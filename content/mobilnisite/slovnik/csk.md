---
slug: "csk"
url: "/mobilnisite/slovnik/csk/"
type: "slovnik"
title: "CSK – Client-Server Key"
date: 2026-01-01
abbr: "CSK"
fullName: "Client-Server Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/csk/"
summary: "Kryptografický klíč používaný v architektuře Generic Bootstrapping Architecture (GBA) standardu 3GPP k zabezpečení komunikace mezi klientem (UE) a aplikačním serverem sítě (NAF). Umožňuje zabezpečený"
---

CSK je kryptografický klíč používaný v architektuře Generic Bootstrapping Architecture (GBA) standardu 3GPP k zabezpečení komunikace mezi klientem a aplikačním serverem sítě, což umožňuje zabezpečený přístup ke službám bez nutnosti samostatného ověření pro každou službu.

## Popis

Klíč Client-Server Key (CSK) je základním bezpečnostním prvkem v architektuře Generic Bootstrapping Architecture ([GBA](/mobilnisite/slovnik/gba/)) standardu 3GPP. Jedná se o kryptografický klíč, typicky odvozený z hlavního relakčního klíče (Ks), který je navázán během procedury [AKA](/mobilnisite/slovnik/aka/) (Authentication and Key Agreement) mezi uživatelským zařízením (UE) a funkcí Bootstrapping Server Function ([BSF](/mobilnisite/slovnik/bsf/)). Proces odvození využívá funkci pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)) se specifickými vstupy, včetně identifikátoru klíče ([B-TID](/mobilnisite/slovnik/b-tid/)), plně kvalifikovaného doménového jména ([FQDN](/mobilnisite/slovnik/fqdn/)) cílové funkce Network Application Function ([NAF](/mobilnisite/slovnik/naf/)) a dalších volitelných parametrů. Tím je zajištěno, že každý CSK je jedinečný pro kombinaci uživatele, relace a konkrétního aplikačního serveru.

Z architektonického hlediska k vytvoření CSK dochází po úspěšném bootstrappingu. UE a BSF nezávisle odvodí stejný klíč Ks_NAF (klíč specifický pro NAF) ze sdíleného klíče Ks. CSK je následně odvozen z tohoto klíče Ks_NAF. BSF poskytne potřebný klíčový materiál (často samotný Ks_NAF nebo jeho referenci) NAF přes rozhraní Zn, zatímco UE vypočítá CSK lokálně. Tato architektura umožňuje NAF ověřit identitu UE a navázat zabezpečený kanál bez přímé účasti na primární proceduře AKA, čímž odlehčuje aplikačním serverům od složitosti ověřování.

V praxi se CSK používá k zabezpečení komunikačního spojení mezi UE a NAF. Může sloužit jako základ pro generování dalších relakčních klíčů pro důvěrnost (šifrování) a ochranu integrity aplikačního protokolu (např. [HTTPS](/mobilnisite/slovnik/https/), SIP). UE při žádosti o službu předloží NAF svůj B-TID. NAF použije tento B-TID k získání odpovídajícího klíčového materiálu z BSF. Obě entity pak nezávisle odvodí stejný CSK, což umožní vzájemné ověření a navázání zabezpečené, šifrované relace. Tento proces je podrobně popsán ve specifikacích jako 3GPP TS 33.220 pro GBA a TS 33.222 pro zabezpečení NAF-UE.

Role CSK je klíčová pro umožnění standardizovaného a zabezpečeného přístupu k IP službám (IMS, lokalizační služby, správa zařízení) v sítích 3GPP. Poskytuje škálovatelnou a efektivní metodu pro ověřování služeb, která eliminuje potřebu, aby UE ukládalo samostatné přihlašovací údaje pro každého poskytovatele služeb. Díky využití robustního zabezpečení AKA založeného na USIM, CSK dědí silné kryptografické vlastnosti, což zajišťuje, že kompromitace jednoho služebního klíče neovlivní ostatní klíče ani přihlašovací údaje pro ověření v jádru sítě.

## K čemu slouží

CSK byl zaveden, aby řešil rostoucí potřebu zabezpečeného ověřování a dohody na klíči pro množství IP služeb nad rámec přístupu k jádru sítě. Před GBA a konceptem CSK musely aplikační servery často implementovat vlastní, potenciálně slabší, ověřovací mechanismy (jako uživatelské jméno/heslo) nebo spravovat složité infrastruktury PKI. To vytvářelo bezpečnostní slabiny, špatnou uživatelskou zkušenost kvůli opakovanému přihlašování a zvyšovalo provozní nároky pro poskytovatele služeb.

Vytvoření CSK bylo motivováno snahou využít silné, SIM kartou založené ověření mobilní sítě pro přidané služby. Řeší problém, jak bezpečně ověřit uživatele u aplikačního serveru třetí strany, aniž by tomuto serveru byla odhalena dlouhodobá tajná hodnota uživatele (Ki). CSK poskytuje mechanismus delegovaného ověření, kdy je důvěra od jádra sítě (HSS/BSF) bezpečně přenesena do aplikační vrstvy. To umožňuje možnosti jednotného přihlášení (SSO) napříč různými službami od stejných nebo různých poskytovatelů.

Historicky, jak se sítě 3GPP vyvíjely k poskytování multimediálních a IoT služeb (např. IMS, M2M komunikace), se stala nezbytnou standardizovaná bezpečnostní architektura řízená operátorem sítě. CSK jako součást GBA tuto architekturu poskytl. Odstranil omezení předchozích ad-hoc přístupů tím, že nabídl standardizovanou, kryptograficky správnou metodu pro odvozování služebně-specifických klíčů z jediného, silného síťového ověření, čímž zvýšil celkovou bezpečnost a interoperabilitu ekosystému.

## Klíčové vlastnosti

- Je odvozen z hlavního relakčního klíče (Ks) navázaného přes AKA, což zajišťuje silný kryptografický původ.
- Je jedinečný pro kombinaci uživatele, bootstrappingové relace a cílové funkce Network Application Function (NAF).
- Umožňuje vzájemné ověření mezi uživatelským zařízením (UE) a aplikačním serverem (NAF).
- Slouží jako kořenový klíč pro generování dalších, relaci-specifických šifrovacích a integritních klíčů.
- Podporuje správu životnosti klíče děděnou z bootstrappingové relace.
- Umožňuje standardizovaný zabezpečený přístup k IMS a dalším IP službám bez nutnosti samostatných přihlašovacích údajů.

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [CSK na 3GPP Explorer](https://3gpp-explorer.com/glossary/csk/)
