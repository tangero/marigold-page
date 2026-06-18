---
slug: "stir"
url: "/mobilnisite/slovnik/stir/"
type: "slovnik"
title: "STIR – Secure Telephone Identity Revisited"
date: 2026-01-01
abbr: "STIR"
fullName: "Secure Telephone Identity Revisited"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/stir/"
summary: "Rámec standardů pro kryptografické ověřování telefonního čísla volající strany, který bojuje proti falšování volajícího čísla (caller ID spoofing) a automatizovaným hovorům (robocalls). Používá digitá"
---

STIR je rámec standardů, který kryptograficky ověřuje telefonní číslo volající strany pomocí digitálních podpisů připojených k signalizaci SIP, aby bojoval proti falšování volajícího čísla (caller ID spoofing) a potvrzoval autorizovaný původ hovoru.

## Popis

Secure Telephone Identity Revisited (STIR) je komplexní rámec standardů 3GPP a [IETF](/mobilnisite/slovnik/ietf/) navržený k obnovení důvěry v identifikaci volajícího tím, že zabraňuje falšování identifikace volající linky ([CLI](/mobilnisite/slovnik/cli/)). V jádru STIR poskytuje mechanismus, pomocí kterého výchozí síť kryptograficky podepíše identitu volajícího (telefonní číslo) a koncová síť tento podpis ověří, než hovor předá volanému. Architektura je založena na decentralizovaném modelu důvěry, kde Autentizační služby ([ATS](/mobilnisite/slovnik/ats/)) ve výchozí síti a Verifikační služby ([VS](/mobilnisite/slovnik/vs/)) v koncové síti provádějí klíčové operace.

Technický pracovní postup začíná při zahájení hovoru. Ve výchozí síti entita podporující STIR (jako [S-CSCF](/mobilnisite/slovnik/s-cscf/) nebo vyhrazená STIR Autentizační služba) vytvoří digitální identifikační token nazvaný PASSporT (Personal Assertion Token). Tento token obsahuje klíčové nároky (claims): číslo volajícího (orig), číslo volaného (dest), čas vydání (iat) a jedinečný identifikátor hovoru. Tento token je následně podepsán pomocí privátního klíče asociovaného s doménou poskytovatele služeb v místě původu. Podepsaný PASSporT je vložen do [SIP](/mobilnisite/slovnik/sip/) INVITE požadavku, typicky do hlavičky Identity, jak je definováno v [RFC](/mobilnisite/slovnik/rfc/) 8224.

Když SIP INVITE prochází sítěmi směrem k cíli, STIR Verifikační služba koncové sítě PASSporT extrahuje. Pro ověření podpisu VS provede sérii kroků. Nejprve určí příslušný veřejný klíč potřebný k ověření. To se provede dotazem na infrastrukturu veřejných klíčů ([PKI](/mobilnisite/slovnik/pki/)), konkrétně pomocí Telephone Identity (TEL) URI volajícího k nalezení příslušné Secure Telephone Identity Governance Authority (STI-GA) a následně Certificate Repository Service (CRS) k získání certifikátu veřejného klíče poskytovatele služeb v místě původu. Po úspěšném ověření podpisu VS potvrdí, že volající číslo nebylo během přenosu změněno a že bylo potvrzeno důvěryhodnou výchozí sítí. Výsledek ověření (např. "verstat: TN-Validation-Passed") je následně přidán do signalizace SIP, což umožňuje koncovému UE nebo síti aplikovat příslušné zacházení, jako je zobrazení symbolu ověření nebo zvýšení priority hovoru.

## K čemu slouží

STIR byl vytvořen pro boj s rostoucím globálním problémem falšování volajícího čísla (caller ID spoofing), který pohání spam, podvody (jako vishing a Wangiri fraud) a automatizované hovory (robocalls). Tradiční signalizační systémy SS7 a SIP používané v telefonních sítích neměly žádný inherentní bezpečnostní mechanismus pro validaci zdroje informací o volajícím čísle. Útočníci mohli snadno vložit falešná čísla do hlavičky "From", což vedlo k rozšířené nedůvěře spotřebitelů v telefonní síť. Tento jev narušil užitečnost hlasových služeb a způsobil významné finanční škody a újmy na soukromí.

Rámec, původně vyvinutý IETF a později přijatý a profilovaný 3GPP počínaje Release 17, byl motivován regulatorním tlakem a potřebou technického řešení v odvětví. Řeší omezení předchozích, často proprietárních řešení pro filtrování hovorů tím, že poskytuje standard pro end-to-end kryptografické ověřování, který funguje napříč administrativními a technologickými hranicemi (např. mezi různými operátory, mezi IP a TDM sítěmi). STIR vytváří řetězec důvěry, kde poskytovatelé služeb ručí za čísla, která přidělují svým účastníkům. Jeho označení "Revisited" (přepracovaný) jej odlišuje od dřívějších, méně komplexních pokusů o zabezpečení volajícího čísla. Tím, že umožňuje ověřené volající číslo, si STIR klade za cíl obnovit důvěru v hlasovou komunikaci, umožnit uživatelům informovaná rozhodnutí o přijetí hovoru a poskytnout základ pro bohatší, důvěryhodné komunikační služby.

## Klíčové vlastnosti

- Kryptografické podepisování a ověřování telefonních čísel volajícího
- Používá digitální identifikační tokeny PASSporT (Personal Assertion Token)
- Decentralizovaný model důvěry založený na přihlašovacích údajích poskytovatele služeb
- Integrace do signalizace SIP prostřednictvím hlavičky Identity (RFC 8224)
- Spoléhá se na infrastrukturu veřejných klíčů (STI-GA/CRS) pro zjišťování klíčů
- Poskytuje výsledky ověření (verstat) pro řízení zacházení s hovorem

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [STIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/stir/)
