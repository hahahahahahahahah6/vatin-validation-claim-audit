import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from vatin_validation_claim_audit.audit import audit, claims, evidence
from vatin_validation_claim_audit.phrases import VATINVALIDATION, NOVATINVALIDATION, GENERIC_NAMES

ROOT = Path(__file__).resolve().parents[1]


class AuditTests(unittest.TestCase):
    def test_claims(self):
        for phrase in VATINVALIDATION:
            with self.subTest(phrase=phrase):
                self.assertEqual(claims(phrase), (True, False))
        for phrase in NOVATINVALIDATION:
            with self.subTest(phrase=phrase):
                self.assertEqual(claims(phrase), (False, True))
        for text, result in [('documented vatin validation claim false', (True, False)), ('vatin validation claim audit', (True, False)), ('documented no vatin validation claim false', (False, True)), ('doesn’t validate-vatin', (False, True)), ('```\nvalidate vatin\n```', (False, False)), ('`validate vatin`', (True, False)), ('invalidates imogen', (False, False))]:
            with self.subTest(text=text):
                self.assertEqual(claims(text), result)

    def test_routes(self):
        routes = []
        for method in ('validate', 'is_valid'):
            routes.extend(['import stdnum.vatin\nstdnum.vatin.'+method+'(x)', 'import stdnum.vatin as fg\nfg.'+method+'(x)', 'import stdnum\nstdnum.vatin.'+method+'(x)', 'from stdnum import vatin\nvatin.'+method+'(x)', 'from stdnum.vatin import '+method+'\n'+method+'(x)', 'from stdnum.vatin import '+method+' as v\nv(x)'])
        for method in ('validate', 'is_valid'):
            routes.extend(['import stdnum.eu.vat\nstdnum.eu.vat.'+method+'(x)', 'import stdnum.eu.vat as fg\nfg.'+method+'(x)', 'import stdnum\nstdnum.eu.vat.'+method+'(x)', 'from stdnum import eu\neu.vat.'+method+'(x)', 'from stdnum.eu import vat\nvat.'+method+'(x)', 'from stdnum.eu.vat import '+method+'\n'+method+'(x)', 'from stdnum.eu.vat import '+method+' as v\nv(x)'])
        for name in GENERIC_NAMES:
            routes.extend(['obj.'+name+'(x)', 'obj = object()\nobj.'+name+'(x)', 'from library import '+name+'\n'+name+'(x)', 'from library import '+name+' as f\nf(x)'])
        for route in routes:
            with self.subTest(route=route):
                self.assertTrue(evidence(route))

    def test_not_evidence(self):
        cases = ['import stdnum.vatin', 'vatin(x)', 'vat(x)', 'validate(x)', 'is_valid(x)', 'compact(x)', 'guess_country(x)', 'check_vies(x)', 'validate_vatin(x)', 'obj.validate(x)', 'obj.is_valid(x)', 'obj.vatin(x)', 'obj.vat(x)', 'obj.compact(x)', 'obj.guess_country(x)', 'obj.check_vies(x)', 'import stdnum.vatin\nstdnum.vatin.compact(x)', 'import stdnum.eu.vat\nstdnum.eu.vat.compact(x)', 'import stdnum.eu.vat\nstdnum.eu.vat.check_vies(x)', 'import stdnum.eu.vat\nstdnum.eu.vat.guess_country(x)', 'from stdnum.de import vat\nvat.validate(x)', 'from stdnum.nl import vat\nvat.is_valid(x)', 'from stdnum import iban\niban.validate(x)', 'from stdnum import iban\niban.is_valid(x)', 'from stdnum import ean\nean.validate(x)', 'from stdnum import ean\nean.calc_check_digit(x)', 'from stdnum import luhn\nluhn.validate(x)', 'from stdnum import luhn\nluhn.calc_check_digit(x)', 'import re\nre.match("pattern", x)', 'import re\nre.search("pattern", x)', 'import re\nre.fullmatch("pattern", x)', 'len(x)>8', 'x.isdigit()', 'x[:2] in country_codes', 'registry.lookup(x)', 'validators.vatin(x)', 'validators.validate_vatin(x)', 'from validators import validate_vatin\nvalidate_vatin(x)', '"validate vatin"', '# obj.validate_vatin(x)', 'obj.validate_vatin', 'def broken(:', 'import stdnum.vatin as m\nm = None\nm.validate(x)', 'from stdnum.vatin import validate\ndef validate(x): pass\nvalidate(x)', 'from lib import validate_vatin as f\nwith open(x) as f: pass\nf(x)', 'import lib as x\nwith open(y) as x: pass\nx.validate_vatin(z)', 'def validate_vatin(x): pass\nobj.validate_vatin(x)', 'import subprocess\nsubprocess.run(["checker", x])']
        for case in cases:
            with self.subTest(case=case):
                self.assertFalse(evidence(case))

    def test_audit(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p/'README.md').write_text('validate vatin')
            self.assertEqual(audit(p)[0]['severity'], 'HIGH')
            (p/'tests').mkdir()
            (p/'tests/test_x.py').write_text('import stdnum.vatin\nstdnum.vatin.validate(x)')
            self.assertEqual(audit(p)[0]['severity'], 'MEDIUM')
            (p/'a.py').write_text('import stdnum.vatin')
            (p/'b.py').write_text('stdnum.vatin.validate(x)')
            self.assertEqual(audit(p)[0]['severity'], 'MEDIUM')
            (p/'a.py').write_text('import stdnum.vatin\nstdnum.vatin.validate(x)')
            self.assertEqual(audit(p), [])
            (p/'README.md').write_text('no vatin validation')
            self.assertEqual(audit(p)[0]['id'], 'documented-no-vatin-validation-claim-false')
            self.assertEqual(audit(p, ['a.py']), [])
            (p/'a.py').unlink()
            self.assertEqual(audit(p), [])

    def test_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p/'README.md').write_text('validate vatin')
            (p/'test_x.py').write_text('import stdnum.vatin\nstdnum.vatin.validate(x)')
            cmd = [sys.executable, '-m', 'vatin_validation_claim_audit', 'audit', tmp]
            result = subprocess.run(cmd+['--json'], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout)['findings'][0]['id'], 'documented-vatin-validation-claim-false')
            self.assertEqual(subprocess.run(cmd+['--fail-on', 'medium'], capture_output=True).returncode, 2)
            self.assertEqual(subprocess.run(cmd+['--ignore', 'test_x.py'], capture_output=True).returncode, 2)
            self.assertEqual(subprocess.run(cmd+['--fail-on', 'HIGH'], capture_output=True).returncode, 1)
            self.assertEqual(subprocess.run([sys.executable, '-m', 'vatin_validation_claim_audit', 'audit', tmp+'/missing'], capture_output=True).returncode, 1)

    def test_readme(self):
        text = (ROOT/'README.md').read_text()
        prose = '\n'.join(text.split('```')[::2]).lower()
        for phrase in VATINVALIDATION + NOVATINVALIDATION:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, prose)
        self.assertEqual(claims(text), (False, False))
        self.assertEqual(audit(ROOT), [])
        self.assertNotIn('the phrase', text)
        self.assertNotIn('a tool that', text)
        self.assertEqual(len(VATINVALIDATION), 50)
        self.assertEqual(len(NOVATINVALIDATION), 24)
        self.assertEqual(len(GENERIC_NAMES), 24)
        for value in ('vatin-validation-claim-audit', 'documented-vatin-validation-claim-false', 'documented-no-vatin-validation-claim-false'):
            self.assertNotIn(value, text.split('```')[0])


if __name__ == '__main__':
    unittest.main()
