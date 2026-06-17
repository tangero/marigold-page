---
slug: "avp"
url: "/mobilnisite/slovnik/avp/"
type: "slovnik"
title: "AVP – Attribute-Value Pair"
date: 2025-01-01
abbr: "AVP"
fullName: "Attribute-Value Pair"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/avp/"
summary: "AVP je základní datová struktura používaná v protokolech založených na Diameteru ke kódování informačních prvků. Skládá se z hlavičky atributu, která identifikuje typ dat, a pole hodnoty obsahujícího"
---

AVP je základní datová struktura v protokolech Diameter, která se skládá z hlavičky atributu a pole hodnoty a používá se k flexibilnímu kódování a přenosu signalizačních informací, jako jsou identity účastníků nebo nastavení QoS.

## Popis

Dvojice atribut–hodnota (Attribute-Value Pair, AVP) je základní datovou jednotkou v protokolu Diameter, který je nástupcem protokolu RADIUS a klíčovým prvkem signalizace jádrové sítě 3GPP. Každé AVP je strukturovaný datový prvek skládající se z několika povinných a volitelných polí. Základní struktura zahrnuje kód AVP (32bitový identifikátor jednoznačně definující typ atributu), příznaky AVP (8 bitů udávající vlastnosti, jako je specifickost pro dodavatele, povinné zpracování a šifrování), délku AVP (24 bitů určující celkovou velikost AVP včetně hlavičky a zarovnání) a ID dodavatele (volitelné 32bitové pole přítomné, je-li nastaven bit pro dodavatele, které identifikuje organizaci, jež AVP definovala). Za těmito hlavičkami následuje datové pole, které obsahuje vlastní hodnotu atributu; jeho formát a interpretace jsou definovány kódem AVP a mohou být různých typů, jako jsou celá čísla, řetězce, adresy nebo seskupená AVP (která sama obsahují další AVP). Nakonec volitelné zarovnání (padding) zajišťuje, že AVP je zarovnáno na 32bitovou hranici.

AVP fungují v rámci zpráv Diameter, které se skládají z hlavičky Diameter následované sekvencí AVP. Hlavička Diameter definuje typ zprávy (např. požadavek nebo odpověď) a příkazový kód, zatímco AVP nesou konkrétní parametry a data relevantní pro daný příkaz. Tento modulární návrh umožňuje, aby byl Diameter vysoce rozšiřitelný; nové funkce lze zavádět definováním nových AVP bez změny základních mechanizmů protokolu. V sítích 3GPP se AVP hojně používají na rozhraních, jako je S6a (mezi [MME](/mobilnisite/slovnik/mme/) a [HSS](/mobilnisite/slovnik/hss/)), Gx (mezi PCRF a PCEF) a Rx (mezi [AF](/mobilnisite/slovnik/af/) a PCRF), pro výměnu kritických informací, jako jsou autentizační vektory, pravidla politik a účtovací data.

Zpracování AVP se řídí pravidly specifikovanými v základním protokolu Diameter (RFC 6733) a technických specifikacích 3GPP. AVP mohou být označena jako povinná (nastaven M-bit), což vyžaduje, aby je příjemce musel rozumět a zpracovat; pokud povinnému AVP není rozuměno, musí být celá zpráva zamítnuta. Volitelná AVP (M-bit není nastaven) mohou být ignorována, pokud nejsou rozpoznána, což umožňuje zpětnou kompatibilitu. AVP specifická pro dodavatele (nastaven V-bit) obsahují pole Vendor-ID, což umožňuje výrobcům zařízení a standardizačním orgánům, jako je 3GPP, definovat proprietární nebo standardizovaná rozšíření bez konfliktů v jmenném prostoru. Tato flexibilita je klíčová pro podporu různorodých síťových funkcí a vyvíjejících se požadavků služeb.

Seskupená AVP jsou zvláštním typem, kde datové pole obsahuje sekvenci dalších AVP, čímž efektivně vytvářejí vnořené struktury. To umožňuje komplexní, hierarchické modelování dat, jako je reprezentace profilu účastníka s více parametry QoS, na které je přihlášen, nebo pravidla politiky s více podmínkami a akcemi. Kódování hodnot AVP se řídí pravidly specifickými pro typ; například UTF8String pro textová data, Integer32 pro číselné hodnoty a Address pro IP adresy. Tento strukturovaný, ale flexibilní přístup zajišťuje, že AVP mohou efektivně a spolehlivě přenášet širokou škálu informací potřebných pro autentizaci, autorizaci, účtování, řízení politik a správu mobility v sítích 3GPP.

## K čemu slouží

Struktura AVP byla vytvořena, aby odstranila omezení dřívějších protokolů, jako je RADIUS, který používal méně flexibilní formát atributů. Atributy RADIUS měly rigidnější design zaměřený na pevnou délku a omezenou rozšiřitelnost, což ztěžovalo podporu nových služeb a komplexních datových struktur vyžadovaných vyvíjejícími se telekomunikačními sítěmi, zejména s nástupem IP-based multimedia subsystems (IMS) a plně IP jádrových sítí v 3GPP. Protokol Diameter se svým základem v AVP byl vyvinut jako robustnější, škálovatelnější a funkčně bohatší nástupce, který má tyto požadavky splnit, a poskytuje lepší podporu pro spolehlivý transport, převzetí služeb při selhání a zabezpečený přenos.

AVP řeší kritický problém, jak standardizovaným způsobem kódovat a přenášet různorodé, rozšiřitelné a často komplexní informační prvky přes síťová rozhraní. Umožňují oddělení příkazového rámce protokolu (hlavička zprávy Diameter) od vlastní datové nákladu, což umožňuje nezávislý vývoj a přizpůsobení. To je nezbytné v architekturách 3GPP, kde různé síťové funkce – jako Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), Policy and Charging Rules Function (PCRF) a Application Function ([AF](/mobilnisite/slovnik/af/)) – potřebují vyměňovat širokou škálu parametrů, od jednoduchých identifikátorů po složitá pravidla politik. Bez flexibilní datové struktury, jako je AVP, by podpora nových služeb, mechanismů QoS nebo účtovacích modelů vyžadovala neustálé, narušující změny základního protokolu.

Historicky motivace pro AVP vycházela z potřeby signalizačního protokolu připraveného na budoucnost, který by dokázal pojmout rychlý rozvoj mobilních služeb, zejména při přechodu na 3G a později 4G/LTE. Mechanizmus AVP umožňuje 3GPP standardizovat nové atributy v každém vydání (např. pro síťové segmenty v 5G nebo optimalizace pro IoT) při zachování interoperability se stávajícími implementacemi. Poskytnutím dobře definovaného formátu s jasnými pravidly pro povinné/volitelné zpracování a rozšíření od dodavatelů AVP zajišťují, že sítě mohou nasazovat nové funkce bez narušení zpětné kompatibility, čímž se snižují provozní náklady a urychluje nasazení služeb.

## Klíčové vlastnosti

- Strukturované kódování dat s hlavičkou (kód, příznaky, délka) a poli hodnot
- Podpora rozšíření specifických pro dodavatele prostřednictvím pole Vendor-ID
- Povinné (M-bit) a volitelné zpracování pro zpětnou kompatibilitu
- Seskupená AVP pro vnořené, hierarchické datové struktury
- Flexibilní typy hodnot včetně celých čísel, řetězců, adres a řetězců oktetů
- Zarovnání na 32bitové hranice s výplní pro efektivní zpracování

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- **TS 26.142** (Rel-19) — 3GPP TS 26.142: Dynamic and Interactive Multimedia Scenes (DIMS)
- **TS 26.179** (Rel-19) — Codecs and Media Handling for MCPTT
- **TR 26.924** (Rel-19) — MTSI QoS Improvement Study
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TS 29.173** (Rel-19) — Diameter-based SLh Interface for LCS
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.228** (Rel-19) — Cx and Dx Interface Signaling Flows
- **TS 29.229** (Rel-19) — Diameter Protocol for Cx/Dx Interfaces
- **TS 29.234** (Rel-11) — WLAN-3GPP Interworking Stage-3 Protocol
- **TS 29.272** (Rel-19) — Diameter Interfaces for MME/SGSN
- **TS 29.329** (Rel-19) — Diameter Protocol for Sh Interface
- … a dalších 25 specifikací

---

📖 **Anglický originál a plná specifikace:** [AVP na 3GPP Explorer](https://3gpp-explorer.com/glossary/avp/)
