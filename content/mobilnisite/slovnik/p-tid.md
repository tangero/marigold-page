---
slug: "p-tid"
url: "/mobilnisite/slovnik/p-tid/"
type: "slovnik"
title: "P-TID – Push Temporary Identifier"
date: 2025-01-01
abbr: "P-TID"
fullName: "Push Temporary Identifier"
category: "Identifier"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/p-tid/"
summary: "Dočasný identifikátor používaný ve službě Push-to-talk over Cellular (PoC) k jednoznačné a anonymní identifikaci PoC klienta během relace. Zajišťuje soukromí uživatele tím, že se vyhne přenosu trvalýc"
---

P-TID je dočasný identifikátor používaný ve službě Push-to-talk over Cellular (PoC) k jednoznačné a anonymní identifikaci klienta během relace, který chrání soukromí uživatele tím, že se vyhne přenosu trvalých identit přes rozhraní.

## Popis

P-TID je identifikátor pro zabezpečení a soukromí definovaný v kontextu služby [OMA](/mobilnisite/slovnik/oma/) Push-to-talk over Cellular (PoC), která je standardizována 3GPP pro integraci s IMS. Jedná se o dočasný alias pro PoC klienta, který generuje a spravuje PoC server. Když se uživatel přihlásí k nebo aktivuje službu PoC, PoC server přiřadí tomuto uživatelskému klientovi P-TID. Tento identifikátor se pak používá v signalizaci PoC relace (např. v [SIP](/mobilnisite/slovnik/sip/) zprávách) a případně v paketech řídicí roviny médií namísto trvalé veřejné identity uživatele, jako je SIP [URI](/mobilnisite/slovnik/uri/) nebo [MSISDN](/mobilnisite/slovnik/msisdn/). Generování P-TID by mělo dodržovat zásady, které zabrání sledování uživatele napříč různými relacemi nebo jeho korelaci s trvalou identitou neoprávněnými stranami. Během navazování PoC relace volající PoC klient zahrne svůj P-TID do pozvánky a PoC server jej použije k identifikaci cílového uživatele, přičemž jej interně mapuje na trvalá předplatitelská data uživatele. Použití P-TID zvyšuje soukromí na referenčním bodě Gm (mezi UE a [P-CSCF](/mobilnisite/slovnik/p-cscf/)) a v samotné vrstvě služby PoC. Je zvláště důležité pro skupinovou komunikaci, kde mohou být pakety řízení relace pozorovány více účastníky. Správa P-TID, včetně jeho životnosti, obnovení a zrušení, je prováděna PoC serverem a jeho formát je specifikován poskytovatelem služby PoC. Identifikátor hraje roli v zákonném odposlechu a korelaci účtování, kde může síťový operátor a poskytovatel služby PoC v rámci svých zabezpečených domén mapovat P-TID zpět na skutečnou identitu uživatele.

## K čemu slouží

P-TID byl vytvořen k řešení problémů se soukromím, které jsou vlastní službám skupinové komunikace push-to-talk. Ve službě jako je PoC, kde jsou řídicí zprávy relace (např. „uživatel X mluví“) vysílány všem členům skupiny, by použití trvalé identity uživatele, jako je telefonní číslo nebo [SIP](/mobilnisite/slovnik/sip/) [URI](/mobilnisite/slovnik/uri/), zbytečně vystavilo tyto citlivé informace všem účastníkům a potenciálně i odposlouchávajícím stranám na rozhraní. P-TID poskytuje vrstvu anonymity, což ztěžuje ostatním uživatelům PoC přímou identifikaci trvalé identity mluvčího. Tím se řeší problém nechtěného sledování uživatelů a vytváření jejich profilů v rámci služby. Dále je v souladu s regulatorními požadavky na soukromí uživatelů v telekomunikacích. Jeho zavedení bylo motivováno specifickou architekturou PoC, která odděluje servisní vrstvu (PoC server) od podkladového jádra IMS, což umožňuje použití službě specifických dočasných identifikátorů. Řeší tak omezení přímého použití IMS Private User Identities ([IMPI](/mobilnisite/slovnik/impi/)) nebo Public User Identities (IMPU) v signalizaci na úrovni služby, které jsou trvalejší a potenciálně citlivé.

## Klíčové vlastnosti

- Dočasný, službě specifický identifikátor pro PoC klienty, přidělovaný PoC serverem.
- Zvyšuje soukromí uživatele zastíráním trvalých identit (MSISDN, SIP URI) v servisní signalizaci.
- Používá se v řídicích protokolech PoC relace (např. v SIP/SDP pro PoC).
- Zabraňuje neoprávněnému sledování uživatele napříč různými PoC relacemi.
- Spravován PoC serverem, včetně generování, přidělování, životnosti a zrušení.
- Umožňuje zákonný odposlech a účtování tím, že umožňuje zabezpečené mapování na skutečnou identitu uživatele v rámci domény operátora.

## Související pojmy

- [POC – Push To Talk Over Cellular](/mobilnisite/slovnik/poc/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [GBA – Generic Bootstrapping Architecture](/mobilnisite/slovnik/gba/)

## Definující specifikace

- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 33.223** (Rel-19) — GBA Push Function Specification
- **TS 33.843** (Rel-15) — Security Study for ProSe UE-to-Network Relay

---

📖 **Anglický originál a plná specifikace:** [P-TID na 3GPP Explorer](https://3gpp-explorer.com/glossary/p-tid/)
