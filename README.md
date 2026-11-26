# Tax-identifier claim audit

This offline tool compares documentation claims with Python call evidence. It parses source without executing it. Review findings in context.

## Usage

```sh
python3 -m vatin_validation_claim_audit audit .
vatin-validation-claim-audit audit . --fail-on medium --json
vatin-validation-claim-audit --version
```

Use `--ignore PREFIX` repeatedly to exclude paths. The default threshold is high; medium includes test-only evidence. Exit codes are 0 for pass, 2 for findings at the threshold, and 1 for usage or input errors.

```text
documented-vatin-validation-claim-false
documented-no-vatin-validation-claim-false
```

## Limitations

A compact call only strips separators and surrounding whitespace and changes case.

A country-module call judges one country only and is not recognised.

A VIES lookup retrieves a record rather than judging the string.

The validators package does not provide the relevant route.

Strings, comments, imports and bare references do not establish a call.

Syntax errors prevent source evidence.

Calls split across modules do not combine into evidence.

A subprocess invocation does not count.

Roadmap, changelog and TODO prose can produce claims without implemented code.

There is no single check digit: NL123456782B90 and NL123456782B91 both pass.

The library does not establish registration with any tax authority.

Separators are stripped before judging.

Greece uses EL instead of GR: EL12345670 validates as EL012345670.

An unknown country code fails: XX1234567890 is rejected.

A regular expression checks a pattern rather than the full library judgement.

A length check alone omits the country-code leg.

A digit-only check alone omits the country-code leg.

The European route covers member states only: BR16727230000197 fails there.

The judgement is country-dependent: the same call applies a different national check per prefix.

A short number fails: FR 40 303 is rejected.

An empty string raises instead of validating.

A country guess does not judge the number.

```text
validate vatin
```

The bare phrase above can describe a manual runbook step.

```text
vatin validation
```

The bare phrase above can describe a roadmap feature.

```text
vatin validator
```

The bare phrase above can describe a hosted web page.

```text
vatin check
```

The bare phrase above can describe a field-presence lint rule.

```text
check vatin
```

The bare phrase above can describe a manual runbook step.

```text
verify vatin
```

The bare phrase above can describe a visual account confirmation.

```text
vatin code validation
```

The bare phrase above can describe a field-presence check.

```text
valid vatin
```

The bare phrase above can appear as example output.

```text
vatin is valid
```

The bare phrase above can appear as example output.

```text
vatin is invalid
```

The bare phrase above can appear as example error text.

```text
vatin validity
```

The bare phrase above can name a configuration flag or column.

```text
vatin format validation
```

The bare phrase above can describe a format without code.

```text
validate vatin number
```

The bare phrase above can describe a shape-only check.

```text
vatin number validation
```

The bare phrase above can name a specification section.

```text
validate vatin code
```

The bare phrase above can describe a manual runbook step.

```text
check vatin code
```

The bare phrase above can describe a manual runbook step.

```text
validate vatin check digit
```

The bare phrase above can describe a manual runbook step.

```text
vatin check digit validation
```

The bare phrase above can name a specification section.

```text
vatin number check
```

The bare phrase above can name an invoicing checklist item.

```text
vatin validation
```

The bare phrase above can describe a result from an external platform.

```text
vatin
```

The bare phrase above alone names a tax identifier without judging it.

```text
vatin number
```

The bare phrase above alone names a number without judging it.

```text
validate identifier
```

The bare phrase above alone does not claim a judgement.

```text
tax identifier
```

The bare phrase above alone does not claim a judgement.

```text
vat number
```

The bare phrase above alone does not claim a judgement.

```text
country code
```

The bare phrase above alone does not claim a judgement.

```text
check digit
```

The bare phrase above alone does not claim a judgement.

```text
VIES
```

The bare phrase above alone does not claim a judgement.

## Differentiation

Other families cover distinct operations: generic validation, ISBN-validation, ISSN-validation, IBAN-validation, UUID-validation, semver-validation, MAC-address-validation, BIC-validation, cron-expression-validation, cron-expression-description, scheduled-execution, date-validation, timeout, payment-processing, credit-card-extraction, auth, password-hashing, password-generation, PDF-encryption, email-sending, SMS-sending, document-extraction, barcode-scanning, email-validation, phone-validation, password-strength, JSON-Schema-validation, credit-card-validation, domain-validation, URL-validation, IP-validation, JSON-parsing, regex, URL-parsing, URL-fetching, DNS, barcode-generation, account-extraction, VIN-extraction, VIN-decoding, VIN-history-lookup, hex-color-validation, ORCID-validation, ISNI-validation, DOI-validation, CASRN-validation, SEDOL-validation, ISIN-validation, ISIN-record-query, ISIN-extraction, CUSIP-validation, IMEI-validation, MEID-validation, ESN-validation, ISMN-validation, ISAN-validation, GRid-validation, EAN-validation, generic-serial-number, FIGI-validation, FIGI-record-query, FIGI-extraction, ISRC-validation, Ethereum-address-validation, Binance-Smart-Chain-address-validation, Tron-address-validation, Litecoin-address-validation, Dogecoin-address-validation, bitcoin-address-validation, transaction-hash-validation, private-key-validation, block-explorer, address-generation, address-extraction, payment-receipt, spreadsheet-reading, spreadsheet-generation, Word-reading, Word-generation, presentation-reading, presentation-generation, PDF-extraction, PDF-generation, PDF-merging, PDF-splitting, PDF-rotation, PDF-form-filling, PDF-watermarking, PDF-redaction, PDF-compression, PDF-annotation, table-extraction, OCR, document-data-extraction, e-signature, screen-recording, video-generation, QR-generation, barcode-generation, barcode-scanning, audio-mixing, audio-generation, audio-editing, audio-source-separation, speech-recognition, speech-synthesis, noise-reduction, music-generation, music-transcription, InChI, SMILES, EC-number, UN-transport-number, PubChem-query, chemical-structure-validation, other-chemical-identifiers, container-number-reading, carrier-registry, BIC-shipowner-code, container-size-type, container-number-generation, ISO-6346-validation, library-record-fetching, library-identifier-registration, cataloguing, OCLC-WorldCat, library-agency-listing, ISIL-validation, IMO-validation, MMSI-validation, HIN-validation, ENI-validation, vessel-registry-lookup, AIS-tracking, ship-name-lookup, IMSI-validation, VIES-lookup, VAT-rate-lookup, tax-calculation, invoice-generation.

## Matched phrases

```text
validate vatin
validates vatin
validating vatin
vatin validation
vatin validations
vatin validator
vatin validation check
validate vatin number
validates vatin number
validating vatin number
vatin number validation
vatin number validator
validate vatin code
validates vatin code
validating vatin code
vatin code validation
vatin code validator
vatin check
check vatin
checks vatin
checking vatin
vatin checker
verify vatin
verifies vatin
verifying vatin
vatin verification
vatin is valid
vatin is invalid
valid vatin
invalid vatin
vatin validity
vatin format validation
validate vatin format
vatin length validation
vatin character validation
is valid vatin
is vatin valid
vatin validation library
vatin validation function
vatin validation tool
vatin code check
check vatin code
verify vatin code
vatin code verification
vatin check digit validation
validate vatin check digit
vatin number check
check vatin number
vatin identifier validation
validate vatin identifier
no vatin validation
does not validate vatin
does not validate vatin number
no vatin validator
no vatin validation check
does not support vatin validation
without vatin validation
vatin validation not supported
vatin validation not available
cannot validate vatin
cannot check vatin
does not check vatin
no vatin check
does not verify vatin
no vatin verification
does not validate vatin code
no vatin code validation
does not check vatin number
no vatin number check
does not verify vatin code
no vatin code verification
vatin validation not implemented
does not validate vatin format
does not validate vatin check digit
```
