---
slug: "aoc-c"
url: "/mobilnisite/slovnik/aoc-c/"
type: "slovnik"
title: "AOC-C – Advice Of Charge - Charging"
date: 2026-01-01
abbr: "AOC-C"
fullName: "Advice Of Charge - Charging"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aoc-c/"
summary: "AOC-C je fakturační služba (charging) dle 3GPP, která uživatelům během hlasových hovorů a datových relací poskytuje informace o poplatcích v reálném čase. Operátorům umožňuje nabízet transparentní účt"
---

AOC-C je fakturační služba (charging) dle 3GPP, která uživatelům během hovorů a datových relací poskytuje informace o poplatcích v reálném čase za účelem transparentního účtování a zabránění neočekávaně vysokým účtům (bill shock).

## Popis

Advice Of Charge - Charging (AOC-C) je komplexní fakturační služba (charging) definovaná ve standardech 3GPP, která mobilním účastníkům poskytuje informace o poplatcích v reálném čase během jejich komunikačních relací. Služba funguje v rámci architektury IP Multimedia Subsystem (IMS) a spolupracuje se systémy účtování, jako jsou Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) a Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)). AOC-C umožňuje operátorům doručovat účtovací upozornění uživatelům různými mechanismy včetně hlášení během hovoru, SMS zpráv nebo vizuálních indikátorů na uživatelském zařízení, což účastníkům umožňuje sledovat náklady na jejich spotřebu během aktivních relací.

Architektonicky je AOC-C integrována s více síťovými elementy včetně Serving-Call Session Control Function (S-CSCF), Application Server ([AS](/mobilnisite/slovnik/as/)) a účtovacích funkcí. Když uživatel zahájí hovor nebo datovou relaci, síť vyvolá účtovací události, které zpracovává účtovací systém. Služba AOC-C následně formátuje tyto informace o poplatcích do uživatelsky přívětivých upozornění, jež mohou být doručena různými rozhraními. Služba podporuje více účtovacích modelů včetně časového, objemového a událostního účtování, s možností poskytovat upozornění v konfigurovatelných intervalech nebo při dosažení specifických prahových hodnot.

Klíčovými komponentami AOC-C jsou funkce AOC-Server, která zpracovává účtovací data, funkce AOC-Client v uživatelském zařízení, která přijímá a zobrazuje upozornění, a účtovací rozhraní propojující se systémy OCS/OFCS. Služba využívá standardizovaná rozhraní Diameter (Ro/Rf) pro komunikaci s účtovacími systémy a signalizaci SIP pro doručování upozornění v rámci IMS relací. AOC-C podporuje scénáře předplacené i postplatby s různými strategiemi upozorňování pro každý fakturační model. Pro předplacené uživatele typicky poskytuje varování o vyčerpání kreditu, zatímco pro uživatele s postplatbou nabízí upozornění na kumulované využití.

Služba hraje v síti klíčovou roli tím, že propojuje technické účtovací systémy s transparentním účtováním směrem k uživateli. Funguje v reálném čase během aktivních relací a sbírá účtovací data z více zdrojů včetně Policy and Charging Rules Function (PCRF) pro datové relace a Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) pro hlasové relace. Upozornění AOC-C mohou obsahovat informace jako kumulované poplatky, zbývající kredit, cena za minutu/kilobajt a odhadované celkové náklady na relaci. Služba také podporuje převod měn a více tarifních zón, což ji činí vhodnou pro scénáře mezinárodního roamingu, kde se složitost účtování výrazně zvyšuje.

## K čemu slouží

AOC-C vznikla jako odpověď na rostoucí potřebu transparentnosti v účtování mobilních telekomunikací, zejména s tím, jak se služby staly komplexnějšími se zavedením IMS a různorodých účtovacích modelů. Před existencí AOC-C účastníci často dostávali neočekávané účty (bill shock) kvůli nedostatku informací o poplatcích v reálném čase během používání služeb. To bylo obzvláště problematické u prémiových služeb, mezinárodního roamingu a datových služeb, kde by se náklady mohly rychle kumulovat bez vědomí uživatele. Služba měla za cíl zvýšit spokojenost zákazníků a snížit spory o účtování prostřednictvím poskytování proaktivních účtovacích upozornění.

Historicky se mobilní operátoři potýkali s rostoucím množstvím stížností zákazníků na neočekávané poplatky, zejména při přechodu na paketově orientované sítě a zavádění přidaných služeb. Tradiční fakturační systémy poskytovaly informace až po spotřebě služby, což uživatele vystavovalo riziku nadměrných výdajů. AOC-C toto řešila integrací schopností účtování v reálném čase přímo do architektury poskytování služeb, což operátorům umožnilo nabízet transparentní účtování jako konkurenční výhodu. Služba byla zvláště důležitá pro předplacené trhy, kde je správa kreditu kritická, a pro trhy s postplatbou, kde uživatelé potřebovali lepší kontrolu nad svými výdaji.

Vytvoření AOC-C v Release 7 časově souviselo s širším nasazením IMS a potřebou sofistikovaných účtovacích mechanismů schopných podporovat konvergované služby. Vyřešila omezení předchozích přístupů, které buď neposkytovaly žádné informace v reálném čase, nebo využívaly proprietární řešení bez interoperability mezi sítěmi. Standardizací AOC-C umožnil 3GPP konzistentní transparentnost účtování napříč různými operátory a regiony, což usnadnilo mezinárodní roaming a interoperabilitu mezi více dodavateli a zároveň dalo uživatelům větší kontrolu nad jejich telekomunikačními výdaji.

## Klíčové vlastnosti

- Upozornění na poplatky v reálném čase během aktivních relací
- Podpora předplacených i postplatbových fakturačních modelů
- Integrace s Online Charging System (OCS) a Offline Charging System (OFCS)
- Více doručovacích mechanismů včetně hlášení během hovoru a SMS
- Podpora převodu měn a mezinárodního roamingu
- Konfigurovatelné prahové hodnoty a intervaly pro upozornění

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 29.364** (Rel-19) — IMS AS Service Data Descriptions
- **TS 29.864** (Rel-8) — Application Server Service Data Definition for IMS Telephony

---

📖 **Anglický originál a plná specifikace:** [AOC-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/aoc-c/)
