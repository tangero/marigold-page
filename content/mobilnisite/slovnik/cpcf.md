---
slug: "cpcf"
url: "/mobilnisite/slovnik/cpcf/"
type: "slovnik"
title: "CPCF – Content Provider Charging Function"
date: 2025-01-01
abbr: "CPCF"
fullName: "Content Provider Charging Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cpcf/"
summary: "CPCF je síťová funkce odpovědná za účtování za služby založené na obsahu, která umožňuje operátorům fakturovat obsah třetích stran. Komunikuje s poskytovateli obsahu a s účtovacím systémem operátora,"
---

CPCF je síťová funkce, která zajišťuje účtování za služby založené na obsahu prostřednictvím rozhraní s poskytovateli obsahu a s účtovacím systémem operátora za účelem generování záznamů pro fakturaci.

## Popis

Content Provider Charging Function (CPCF) je specializovaný síťový prvek definovaný v architektuře 3GPP, který usnadňuje účtování za služby zahrnující obsah třetích stran. Funguje jako prostředník mezi externími poskytovateli obsahu a základní účtovací infrastrukturou mobilního operátora, konkrétně Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) a Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)). Primární rolí CPCF je převod využití služeb a událostí specifických pro obsah na standardizované záznamy o účtovacích datech ([CDR](/mobilnisite/slovnik/cdr/)) nebo na účtovací zprávy založené na protokolu Diameter, které mohou systémy operátora zpracovat. To zahrnuje identifikaci poskytovatele obsahu, typu obsahu (např. video stream, stažení hry, sponzorovaná aplikace) a aplikaci příslušného tarifu nebo účtovací politiky dohodnuté v obchodním vztahu mezi operátorem a poskytovatelem obsahu.

Z architektonického hlediska je CPCF typicky umístěn ve vrstvě služeb nebo jako součást specializované funkce účtovací brány. Komunikuje s aplikačními servery (jako jsou ty v IP Multimedia Subsystem nebo IMS) nebo přímo s platformami pro doručování obsahu, aby přijímal oznámení o zahájení, změně a ukončení služby obsahu. Mezi klíčové vnitřní komponenty patří modul vynucování politik, který aplikuje účtovací pravidla na základě identifikátorů služeb a profilů uživatelů, a mediační funkce, která formátuje účtovací informace do formátů vyhovujících specifikacím 3GPP, jako jsou zprávy Diameter Credit-Control-Request ([CCR](/mobilnisite/slovnik/ccr/)) a Credit-Control-Answer ([CCA](/mobilnisite/slovnik/cca/)) pro online účtování, nebo vytváří Charging Data Records (CDR) pro offline účtování. CPCF může také udržovat databázi nebo komunikovat s úložištěm profilů předplatitelů, aby ověřila oprávnění uživatelů ke konkrétním službám obsahu.

Během provozu, když uživatel přistupuje k placené službě obsahu, obslužný síťový uzel (např. Proxy-Call Session Control Function nebo aplikační server) odešle účtovací požadavek CPCF. CPCF požadavek ověří, identifikuje zapojeného poskytovatele obsahu pomocí parametrů, jako je identifikátor poskytovatele obsahu, a určí použitelný účtovací model – který může být založen na událostech (např. jednorázový poplatek za stažení aplikace), na relaci (např. účtování za minutu streamování videa) nebo na objemu dat (např. účtování za spotřebovaná data). Pro online účtování komunikuje v reálném čase s OCS, aby zkontrolovala kredit a rezervovala jednotky předtím, než službu povolí. Pro offline účtování generuje CDR, které jsou později přeneseny do fakturační domény pro vyúčtování. Toto oddělení zajišťuje, že poskytovatelé obsahu mohou mít flexibilní, přizpůsobené účtovací dohody bez nutnosti hluboké integrace do účtovacích systémů jádra sítě operátora.

Role CPCF je klíčová pro umožnění moderního ekosystému mobilních služeb. Podporuje složité obchodní modely, jako je 'toll-free' nebo sponzorovaný přenos dat, kdy poskytovatel obsahu platí za datové využití vzniklé koncovými uživateli při přístupu k jeho službě, čímž odstraňuje cenové bariéry pro uživatele. Také umožňuje nabídky prémiového obsahu, kde operátoři mohou specifický obsah zabalit do datových tarifů. Poskytnutím standardizovaného rozhraní (specifikovaného v 3GPP TS 32.260 pro správu účtování) CPCF snižuje složitost integrace pro operátory i poskytovatele obsahu, což podporuje živější a zpeněžitelný trh s mobilním obsahem. Její funkcionalita je často integrována s širšími architekturami řízení politik a účtování (PCC), aby zajistila souvislé poskytování služeb a jejich zpeněžení.

## K čemu slouží

CPCF byla vytvořena, aby řešila rostoucí potřebu mobilních operátorů efektivně zpeněžit obsah a služby třetích stran doručované přes jejich sítě. Před její standardizací bylo účtování za obsah často řešeno pomocí ad-hoc proprietárních rozhraní mezi obsahovými platformami a fakturačními systémy, což vedlo k integračním výzvám, omezené škálovatelnosti a obtížím při podpoře scénářů účtování v reálném čase. To brzdilo vývoj inovativních služeb, jako jsou sponzorovaná data, prémiové video a účtování založené na aplikacích. CPCF poskytuje standardizovaný mechanismus definovaný 3GPP, který tuto mezeru překlenuje a umožňuje jasné, ověřitelné a flexibilní finanční vypořádání mezi operátory a poskytovateli obsahu.

Historicky, jak se mobilní sítě vyvíjely z primárně hlasově orientovaných na datově orientované platformy se zavedením 3G a později 4G, hodnota se přesunula k over-the-top ([OTT](/mobilnisite/slovnik/ott/)) obsahu a aplikacím. Operátoři se snažili přestat být pouhými 'přenašeči bitů' a podílet se na výnosech generovaných obsahem. CPCF, zavedená ve 3GPP Release 5 spolu s IP Multimedia Subsystem (IMS), byla součástí širšího rámce pro umožnění účtování založeného na službách. Vyřešila problém, jak standardizovaným způsobem přisoudit využití sítě a spotřebu služeb konkrétním poskytovatelům obsahu, což umožnilo sofistikované účtovací modely, jako je zpětné účtování (kde platí poskytovatel) nebo rozdělené účtování.

Tato technologie řeší omezení předchozích přístupů oddělením logiky účtování za obsah od účtování v jádru sítě. Namísto požadavku, aby každý poskytovatel obsahu přímo komunikoval se složitými telekomunikačními účtovacími systémy, jako je [OCS](/mobilnisite/slovnik/ocs/), funguje CPCF jako jednotná brána. To zjednodušuje obchodní a technický proces připojování pro poskytovatele obsahu, snižuje režii operátora a zajišťuje, že účtovací data odpovídají standardům 3GPP pro konzistenci a spolehlivost ve fakturaci. Umožňuje operátorům nabízet nové, konkurenceschopné servisní balíčky a partnerství, což nakonec podporuje využití dat a spokojenost zákazníků.

## Klíčové vlastnosti

- Standardizované rozhraní pro účtování poskytovatelům obsahu (3GPP TS 32.260)
- Podpora online (v reálném čase) a offline (dávkových) účtovacích modelů
- Mediační funkce pro generování Charging Data Records (CDR) vyhovujících specifikacím 3GPP
- Integrace s architekturou Policy and Charging Control (PCC) pro jednotné vynucování politik
- Umožňuje složité fakturační modely jako sponzorovaná data, prémiový obsah a účtování založené na událostech
- Ověřuje a identifikuje poskytovatele obsahu pro přesné finanční vypořádání

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [OFCS – Offline Charging System](/mobilnisite/slovnik/ofcs/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.815** (Rel-5) — IMS Charging Implications
- **TS 32.260** (Rel-19) — IMS Charging Management

---

📖 **Anglický originál a plná specifikace:** [CPCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpcf/)
