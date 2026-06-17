---
slug: "erp"
url: "/mobilnisite/slovnik/erp/"
type: "slovnik"
title: "ERP – EAP Re-authentication Protocol"
date: 2025-01-01
abbr: "ERP"
fullName: "EAP Re-authentication Protocol"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/erp/"
summary: "Protokol umožňující rychlou a efektivní přeauthentizaci uživatele nebo zařízení bez nutnosti provedení plné EAP autentizační výměny. Snižuje signalizační režii a latenci při předávání spojení nebo obn"
---

ERP je protokol, který umožňuje rychlé přeauthentizování bez plné EAP výměny, čímž snižuje signalizační režii a latenci pro plynulou mobilitu při předávání spojení v 3GPP a ne-3GPP sítích.

## Popis

[EAP](/mobilnisite/slovnik/eap/) Re-authentication Protocol (ERP) je bezpečnostní protokol definovaný v rámci frameworku Extensible Authentication Protocol (EAP), standardizovaný [IETF](/mobilnisite/slovnik/ietf/) a přijatý 3GPP. Jeho primární funkcí je provedení odlehčené přeauthentizace již dříve authentizovaného uzlu (např. UE) při jeho přesunu mezi přístupovými body nebo při potřebě obnovit jeho bezpečnostní kontext, aniž by bylo nutné znovu provádět výpočetně náročnou a časově zdlouhavou plnou EAP metodu. ERP toho dosahuje využitím kryptografického materiálu odvozeného z počáteční plné EAP autentizace, konkrétně Master Session Key ([MSK](/mobilnisite/slovnik/msk/)) a Extended Master Session Key ([EMSK](/mobilnisite/slovnik/emsk/)). Z těchto klíčů jsou odvozeny Re-authentication Root Key (rRK) a následně Re-authentication Integrity Key (rIK) a Re-authentication Encryption Key (rEK), které tvoří bezpečný základ pro zkrácenou výměnu.

Z architektonického hlediska se ERP účastní tři entity: uzel (UE), autentizátor (např. přístupový bod nebo eNodeB/gNodeB) a backendový autentizační server (např. [AAA](/mobilnisite/slovnik/aaa/) server). Protokol funguje tak, že uzel iniciuje žádost o přeauthentizaci pomocí vyhrazené EAP metody, EAP-Initiate/Re-auth. Tuto žádost autentizátor zpracuje lokálně, pokud disponuje potřebným rIK, nebo ji přepošle backendovému serveru. Výměna zahrnuje minimální počet zpráv, typicky pouze žádost a odpověď, které obsahují kryptograficky chráněná sekvenční čísla a identifikátory pro prevenci replay útoků. Úspěšné dokončení vede k odvození nového klíčového materiálu (nové MSK) pro novou relaci, čímž je zajištěna forward secrecy.

Role ERP v ekosystému 3GPP je nedílnou součástí umožnění bezpečného a rychlého předávání spojení, zejména ve scénářích zahrnujících interoperabilitu ne-3GPP přístupu (jako Wi-Fi) s jádrem 3GPP, jak je definováno v architekturách Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)) a Non-3GPP InterWorking Function ([N3IWF](/mobilnisite/slovnik/n3iwf/)). Je klíčovou součástí pro optimalizaci výkonu procedur authentication, authorization, and accounting (AAA) během událostí mobility. Díky drastickému snížení autentizační latence z potenciálních stovek milisekund na desítky milisekund ERP přímo přispívá ke zlepšení uživatelského zážitku u aplikací citlivých na latenci a podporuje požadavky na plynulou mobilitu systémů 5G a dalších generací.

## K čemu slouží

ERP byl vytvořen k řešení významného výkonnostního omezení, které představuje plná [EAP](/mobilnisite/slovnik/eap/) autentizace při častých událostech mobility. V mobilních sítích, zejména s rozšířením heterogenního přístupu (např. přepínání mezi celulární sítí a Wi-Fi), může zařízení potřebovat přeauthentizaci často. Plná EAP výměna zahrnuje několik kol výměny zpráv s potenciálně vzdáleným AAA serverem, což přináší značnou latenci a signalizační zátěž jak v rádiové, tak v jádrové síti. To by mohlo vážně narušit kontinuitu služeb a způsobit znatelné přerušení hovorů nebo videohovorů během předávání spojení.

Motivace vycházela z potřeby standardizované, kryptograficky robustní metody pro rychlé znovunastavení důvěry a relaních klíčů. Před ERP byla řešení často proprietární nebo spoléhala na stavový přenos kontextu mezi síťovými uzly, což mělo omezení ve škálovatelnosti a bezpečnosti. ERP poskytuje bezstavové, protokolové řešení, kde bezpečnost přeauthentizace je založena na klíčích z počáteční autentizace. Jeho vývoj byl hnáň požadavky z práce 3GPP na System Architecture Evolution (SAE) a později 5G, které vyžadují efektivní bezpečnou mobilitu napříč více přístupovými technologiemi.

Řešením problému latence přeauthentizace ERP umožňuje praktickou implementaci funkcí jako plynulé offloadování do důvěryhodných a nedůvěryhodných ne-3GPP sítí, rychlé znovupřipojení po krátkých odpojeních a efektivní podpora masivního množství IoT zařízení, která mohou často přecházet do režimu spánku a probouzet se. Je základním prvkem pro dosažení cílů nízké latence a vysoké spolehlivosti moderních celulárních systémů.

## Klíčové vlastnosti

- Umožňuje kryptograficky bezpečnou přeauthentizaci bez provedení plné EAP metody
- Odvozuje nové relaní klíče (MSK) z Re-authentication Root Key (rRK)
- Pro výměnu využívá protokol EAP-Initiate/Re-auth
- Minimalizuje autentizační latenci a signalizační režii během předávání spojení
- Podporuje mobilitu mezi 3GPP a ne-3GPP přístupovými sítěmi
- Poskytuje ochranu proti replay útokům prostřednictvím sekvenčních čísel a kryptografického provázání

## Související pojmy

- [EAP – Extensible Authentication Protocol](/mobilnisite/slovnik/eap/)
- [AAA – Authentication, Authorization, and Accounting](/mobilnisite/slovnik/aaa/)
- [N3IWF – Non-3GPP access InterWorking Function](/mobilnisite/slovnik/n3iwf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 26.962** (Rel-19) — ITT4RT Operation and Usage Guidelines
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [ERP na 3GPP Explorer](https://3gpp-explorer.com/glossary/erp/)
