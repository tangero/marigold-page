---
slug: "nanp"
url: "/mobilnisite/slovnik/nanp/"
type: "slovnik"
title: "NANP – North American Numbering Plan"
date: 2025-01-01
abbr: "NANP"
fullName: "North American Numbering Plan"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nanp/"
summary: "Telefonní číslovací plán pro Spojené státy, Kanadu, Bermudy a různé karibské národy. Definuje strukturu telefonních čísel (např. NPA-NXX-XXXX) a je integrován do standardů 3GPP, aby zajistil správné s"
---

NANP je telefonní číslovací plán pro Spojené státy, Kanadu, Bermudy a části Karibiku, který definuje struktury čísel pro správné směrování hovorů a SMS v mobilních sítích 3GPP.

## Popis

North American Numbering Plan (NANP) je komplexní, integrovaný systém telefonního číslování spravovaný správcem North American Numbering Plan Administrator (NANPA). V kontextu 3GPP se nejedná o síťový prvek, ale o kritický externí číslovací plán, který musí mobilní síť rozpoznat, interpretovat a správně zpracovat. NANP definuje standardní 10místný formát telefonních čísel, strukturovaný jako 3místný kód číslovací oblasti (Numbering Plan Area, NPA) (často nazývaný směrové číslo), 3místný kód ústředny (Central Office, NXX) a 4místné účastnické číslo (XXXX). Tento formát je vložen do mezinárodního čísla E.164 přidáním předvolby země '1' (např. +1-212-555-1234).

Sítě 3GPP integrují podporu NANP na více úrovních. V jádru sítě, konkrétně v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)), Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a funkcích řízení hovorových relací, se provádí analýza číslování. Při zpracování volání nebo [SMS](/mobilnisite/slovnik/sms/) iniciovaného mobilním zařízením ([MO](/mobilnisite/slovnik/mo/)) síť analyzuje vytočené číslice. Pokud číslo odpovídá vzorům NANP (začíná '+1'), je zacházeno podle specifických pravidel směrování definovaných pro region NANP. To zahrnuje porozumění speciálním kódům NPA, jako jsou bezplatná čísla (800, 888 atd.), prémiová čísla nebo nouzová čísla (911). Pro příchozí hovory ([MT](/mobilnisite/slovnik/mt/)) musí síť správně směrovat mezinárodní hovory určené pro čísla NANP přes příslušné brány a rozhraní mezi operátory.

Zpracování zahrnuje několik prvků protokolů. V signalizačních protokolech, jako je [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part) a [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol), je číslo NANP přenášeno v konkrétních polích. Síť musí také zvládat přenositelnost čísel v rámci regionu NANP, kde si účastník může ponechat své číslo při změně poskytovatele služeb nebo lokality. To vyžaduje dotazy na databáze přenositelnosti čísel (jako je LNPA v USA). Dále pro služby jako SMS a MMS musí být formát NANP správně prezentován a uložen v telefonním seznamu zařízení a na SMSC/MMSC. Specifikace 3GPP zajišťují, že zařízení a síťové prvky po celém světě mohou tato čísla jednotně zpracovávat, což umožňuje bezproblémovou globální interoperabilitu pro účastníky v regionu NANP a pro komunikaci s tímto regionem.

## K čemu slouží

NANP byl vytvořen dlouho před buněčnými sítěmi, aby přinesl řád a efektivitu do rozšiřující se telefonní sítě v Severní Americe. Jeho primárním účelem byla automatizace dálkového vytáčení a strukturovaná správa vyčerpávání telefonních čísel. Pro 3GPP je účelem specifikace a podpory NANP zajistit, aby globální mobilní sítě mohly správně spolupracovat s pevnými a mobilními sítěmi v regionu NANP, který představuje významnou ekonomickou a komunikační zónu.

Bez explicitní podpory by evropská nebo asijská mobilní síť mohla špatně interpretovat číslo NANP (jako +1-202-555-0123) kvůli jeho jedinečné struktuře a sdílenému kódu země '1' pro více národů. To by mohlo vést k chybnému směrování hovorů, nedoručení SMS nebo nesprávnému účtování. Standardy 3GPP integrují pravidla NANP, aby tyto problémy interoperability vyřešily. Definují, jak analyzovat 10místný formát NANP z čísla E.164, jak aplikovat národně specifické směrování pro hovory v rámci kódu země '+1' a jak zpracovávat regionálně specifické služby, jako je nouzové volání 911 nebo bezplatná čísla 800. Tato podpora je klíčová pro umožnění roamingu, a to jak pro účastníky z regionu NANP cestující do zahraničí, tak pro mezinárodní návštěvníky roamingující v Severní Americe, a zajišťuje, že jejich zařízení a navštívené sítě rozumí místním formátům čísel.

## Klíčové vlastnosti

- Definuje 10místný formát čísla (NPA-NXX-XXXX) pro Severní Ameriku
- Používá jednotný kód země '+1' pro více zemí/území
- Zahrnuje speciální služební kódy (např. 911 pro nouzové volání, 800 pro bezplatná čísla)
- Vyžaduje síťovou podporu pro přenositelnost čísel v rámci plánu
- Integrován do řízení hovorů, SMS a správy účastnických dat v 3GPP
- Nezbytný pro správné směrování a účtování meziregionálních hovorů a zpráv

## Související pojmy

- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization

---

📖 **Anglický originál a plná specifikace:** [NANP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nanp/)
