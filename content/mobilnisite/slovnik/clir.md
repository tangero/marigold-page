---
slug: "clir"
url: "/mobilnisite/slovnik/clir/"
type: "slovnik"
title: "CLIR – Calling Line Identification Restriction"
date: 2025-01-01
abbr: "CLIR"
fullName: "Calling Line Identification Restriction"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/clir/"
summary: "Doplňková služba, která umožňuje volající straně zabránit zobrazení svého telefonního čísla straně volané. Poskytuje ochranu soukromí omezením přenosu identity volající linky (CLI) v signalizačních zp"
---

CLIR je doplňková služba, která zabraňuje zobrazení telefonního čísla volajícího straně volané tím, že omezí jeho přenos během sestavování hovoru.

## Popis

Calling Line Identification Restriction (CLIR) je standardizovaná doplňková služba v sítích 3GPP, která umožňuje volajícímu účastníkovi omezit prezentaci své identity volající linky ([CLI](/mobilnisite/slovnik/cli/)) volané straně. Služba funguje úpravou signalizačních zpráv vyměňovaných během sestavování hovoru, konkrétně v rámci zprávy Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)) v [ISUP](/mobilnisite/slovnik/isup/) nebo zprávy Setup v protokolech [ISDN](/mobilnisite/slovnik/isdn/)/BICC. Při aktivaci CLIR síť buď vynechá informační element čísla volající strany, nebo jej označí jako 'prezentace omezena' podle trvalého předplatného služby účastníka nebo dočasné aktivace pomocí prefixu (např. *67).

Technická implementace zahrnuje více síťových prvků. Původní Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)) vyhodnotí profil služeb volajícího účastníka, který je uložen v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Na základě nastavení předplatného CLIR účastníka – které může být 'permanentní' (platí pro všechny hovory) nebo 'výchozí' (s možností přepsání) – MSC manipuluje s polem 'Presentation Indicator' v informačním elementu čísla volající strany. Při trvalém omezení je CLI konzistentně zadrženo. Při výchozím nastavení může účastník použít prefix k aktivaci omezení pro konkrétní hovor nebo příponu k povolení prezentace pro konkrétní hovor.

V signalizaci jádra sítě CLIR interaguje se službou Calling Line Identification Presentation (CLIP) na terminující straně. Když dorazí hovor s omezeným CLI k terminujícímu MSC, je zkoumán indikátor prezentace. Pokud je označen jako 'omezeno', terminující síť nedoručí CLI k terminálu volané strany, nebo může zobrazit 'privátní číslo', 'anonymní' apod. Služba také funguje ve spojení s dalšími doplňkovými službami, jako je Connected Line Identification Presentation (COLP), a musí zvládat různé scénáře včetně mezinárodních hovorů, kde mohou omezení upravovat národní předpisy.

Architektura služby zajišťuje zpětnou kompatibilitu a spolupráci se staršími sítěmi (PSTN, ISDN). Ve sítích typu all-IP (IMS) je CLIR implementována pomocí SIP hlaviček, konkrétně hlavičky P-Asserted-Identity s indikátory ochrany soukromí. Serving-Call Session Control Function (S-CSCF) aplikuje profil účastníka k nastavení příslušných privátních hlaviček. CLIR je základní funkce ochrany soukromí, která funguje transparentně napříč okruhově i paketově přepínanými doménami, zachovává soukromí uživatele a zároveň zajišťuje dokončení hovoru.

## K čemu slouží

CLIR byla vytvořena pro řešení rostoucích obav o soukromí v telekomunikacích, což umožňuje jednotlivcům a organizacím kontrolovat zveřejnění svých telefonních čísel. Před její standardizací neměli volající standardizovanou metodu, jak zabránit zobrazení svého čísla, což mohlo vést k nežádanému kontaktu, obtěžování nebo porušení důvěrnosti v citlivých situacích (např. zdravotnictví, vymáhání práva, případy domácího násilí). Služba poskytuje zásadní rovnováhu mezi právem volané strany vědět, kdo volá, a právem volající strany na soukromí.

Historicky se služby zobrazení volajícího (CLIP) staly populárními v 80. a 90. letech 20. století, což vytvořilo poptávku po odpovídající schopnosti omezení. 3GPP standardizovala CLIR ve vydání Release 99, aby zajistila konzistentní implementaci napříč sítěmi GSM, UMTS a později LTE/5G, a nahradila tak proprietární řešení. Služba řeší problém nedobrovolného zveřejnění osobních údajů, což je obzvláště důležité s nástupem mobilních telefonů, kde jsou čísla osobněji identifikovatelná než pevná linková čísla.

CLIR také řeší obchodní potřeby, kdy společnosti chtějí chránit svá internální čísla přípon nebo přímé linky operátorů call centra. Umožňuje dodržování předpisů na ochranu soukromí (např. GDPR) tím, že poskytuje technické prostředky k zadržení osobních údajů. Flexibilní implementace služby – umožňující jak trvalé předplatné, tak aktivaci pro jednotlivé hovory – vyhovuje různým uživatelským preferencím při zachování síťové efektivity a interoperability mezi různými operátory a zeměmi s různými zákony na ochranu soukromí.

## Klíčové vlastnosti

- Umožňuje trvalé nebo dočasné omezení zobrazení čísla volajícího
- Používá standardizovanou signalizaci v protokolech ISUP, ISDN a SIP
- Spolupracuje se službou CLIP v terminující síti
- Podporuje aktivaci pro jednotlivé hovory pomocí prefixových kódů (např. *67)
- Udržuje soukromí napříč mezinárodními síťovými hranicemi
- Integruje se se správou profilů účastníka v HLR/HSS

## Související pojmy

- [CLIP – Calling Line Identification Presentation](/mobilnisite/slovnik/clip/)
- [COLP – Connected Line identification Presentation](/mobilnisite/slovnik/colp/)
- [COLR – Connected Line identification Restriction](/mobilnisite/slovnik/colr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TR 22.976** (Rel-2) — Release 2000 Services Overview
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 24.407** (Rel-8) — OIP and OIR Simulation Services Protocol
- **TS 24.607** (Rel-19) — OIP and OIR Supplementary Services Stage 3

---

📖 **Anglický originál a plná specifikace:** [CLIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/clir/)
