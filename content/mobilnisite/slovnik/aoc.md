---
slug: "aoc"
url: "/mobilnisite/slovnik/aoc/"
type: "slovnik"
title: "AOC – Advice Of Charge"
date: 2025-01-01
abbr: "AOC"
fullName: "Advice Of Charge"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aoc/"
summary: "Advice Of Charge (AOC) je služba 3GPP, která poskytuje uživatelům informace o ceně v reálném čase během komunikační relace. Umožňuje uživatelům sledovat náklady za využití před, během a po hovorech či"
---

AOC je služba 3GPP, která poskytuje uživatelům informace o ceně v reálném čase během komunikační relace, například hovoru nebo datové relace, aby podpořila transparentnost a kontrolu nákladů.

## Popis

Advice Of Charge (AOC) je standardizovaná služba v rámci architektury 3GPP navržená k poskytování detailních informací o poplatcích vznikajících z telekomunikačního využití účastníkům v reálném čase. Funguje napříč různými doménami, včetně hlasových hovorů, zpráv a datových relací, a je nedílnou součástí jak přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)), tak přepojování paketů (PS). Služba využívá fakturační a účtovací systémy jádra sítě, komunikuje s entitami jako je Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) a Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) pro získání tarifních a využívacích dat. AOC zajišťuje, že jsou informace o ceně přesně vypočteny a formátovány pro doručení na uživatelský terminál (UE), typicky pomocí in-band signalizace nebo zpráv doplňkových služeb, což umožňuje okamžitou zpětnou vazbu během aktivních relací.

Architektonicky zahrnuje AOC několik klíčových síťových komponent. V CS doméně komunikuje s Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Visitor Location Register (VLR) pro manipulaci s cenou související s hovory, zatímco v PS doméně spolupracuje se Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) a Packet Data Network Gateway (PGW) pro datové relace. Služba využívá standardizované protokoly, například Diameter pro interakce s online účtováním, ke komunikaci mezi síťovými prvky a účtovacími systémy. Zprávy AOC jsou strukturovány dle specifikací 3GPP (např. TS 24.186, TS 29.658) a mohou obsahovat detaily jako tarifní sazby, kumulované náklady a zbývající kredit, které jsou zobrazeny na uživatelském rozhraní terminálu (UE).

Služba funguje na základě spouštění účtovacích událostí v reakci na akce účastníka, například zahájení hovoru nebo datové relace. Když začne relace s podporou AOC, síť vyvolá účtovací procedury, které dotazují OCS nebo offline účtovací systémy pro stanovení platných sazeb. Tyto informace jsou následně předány do UE prostřednictvím vyhrazené signalizace, například USSD zpráv nebo hlasových hlášení během hovoru, podle konkrétní implementace. Například během hovoru může AOC poskytovat pravidelné aktualizace o délce hovoru a nákladech, zatímco u dat může uživatele upozornit po dosažení určitého datového prahu. Služba podporuje více fází: [AOC-S](/mobilnisite/slovnik/aoc-s/) (při navázání relace), [AOC-D](/mobilnisite/slovnik/aoc-d/) (během relace) a AOC-E (při ukončení relace), čímž zajišťuje komplexní pokrytí od začátku do konce.

Role AOC v síti přesahuje rámec uživatelského pohodlí; jedná se o kritickou komponentu pro regulatorní shodu a diferenciaci operátorů. Nabídkou transparentního účtování operátoři snižují spory se zákazníky a zvyšují jejich spokojenost, zvláště v roamingu, kde mohou být náklady nejasné. Služba se také integruje s mechanismy řízení politik, což operátorům umožňuje vynucovat limity výdajů nebo nabízet přizpůsobené tarifní plány. V moderních sítích se AOC vyvinulo tak, aby podporovalo služby založené na IMS, umožňujíc účtování za multimediální relace a over-the-top aplikace, čímž si zachovává relevanci v čistě IP prostředích. Jeho implementace vyžaduje pečlivou koordinaci mezi funkcemi účtování, signalizace a uživatelské roviny, aby bylo zajištěno přesné a včasné poskytování informací bez snížení kvality služby.

## K čemu slouží

AOC bylo vytvořeno, aby řešilo nedostatek transparentnosti v telekomunikačním účtování, což historicky vedlo k 'překvapení z účtu' u účastníků nevědomých si kumulujících se poplatků, zejména při roamingu nebo při využívání prémiových služeb. Před jeho standardizací uživatelé často dostávali detailní informace o cenách až na měsíčních výpisech, což ztěžovalo reálnou kontrolu výdajů. To bylo zvláště problematické pro předplacené zákazníky, kterým hrozilo neočekávané přerušení služby při vyčerpání kreditu. AOC tyto problémy řeší poskytnutím okamžitých, akčních informací o ceně, což uživatelům umožňuje činit informovaná rozhodnutí o svém využívání a vyhýbat se neočekávaným nákladům.

Motivace pro AOC vycházela jak z požadavků spotřebitelů, tak z regulatorních tlaků za spravedlivější účtovací praxi. Jak se mobilní služby rozšiřovaly na konci 90. let a začátkem roku 2000, operátoři se potýkali s rostoucím počtem stížností na netransparentní účtování, což narušovalo důvěru a zákaznickou loajalitu. 3GPP zavedlo AOC ve verzi 8 jako součást širšího úsilí o zvýšení transparentnosti služeb a sladění s globálními telekomunikačními standardy. Řešilo omezení dřívějších proprietárních řešení, která byla nekonzistentní mezi sítěmi a zařízeními a bránila interoperabilitě. Standardizací AOC umožnilo 3GPP bezproblémová upozornění na ceny napříč různými operátory a regiony, což usnadnilo roamingové dohody a zlepšilo uživatelský zážitek.

Dále AOC podporuje obchodní cíle tím, že umožňuje operátorům nabízet služby s přidanou hodnotou, jako jsou upozornění na přizpůsobené tarify nebo kontroly výdajů, což může jejich nabídky odlišit na konkurenčních trzích. Rovněž napomáhá regulatorní shodě, protože mnoho jurisdikcí vyžaduje jasné sdělování poplatků spotřebitelům. Vývoj služby odráží průběžné potřeby, jako je adaptace na IP založené sítě a různé typy služeb, což zajišťuje její relevanci v éře komplexních cenových modelů pro data, hlas a multimedia. Nakonec AOC vyvažuje posílení postavení uživatele s provozní efektivitou, snižuje náklady na podporu související s dotazy na účtování a zároveň podporuje transparentnější telekomunikační ekosystém.

## Klíčové vlastnosti

- Zobrazení informací o ceně v reálném čase během aktivních relací
- Podpora více fází: navázání (AOC-S), během (AOC-D) a ukončení (AOC-E)
- Integrace s Online Charging System (OCS) a offline účtovacími systémy
- Kompatibilita s doménami přepojování okruhů (CS) a přepojování paketů (PS)
- Standardizované protokoly jako Diameter pro účtovací interakce
- Upozornění uživatelů pomocí USSD, in-band signalizace nebo rozhraní zařízení

## Definující specifikace

- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.642** (Rel-19) — CCBS/CCNR/CCNL SIP Protocol Specification
- **TS 24.647** (Rel-19) — Advice of Charge (AOC) service protocol
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.458** (Rel-8) — SIP Transfer of Tariff Info for Charging
- **TS 29.658** (Rel-19) — SIP Transfer of Tariff Information
- **TS 32.850** (Rel-14) — IMS Charging Correlation Methods Study

---

📖 **Anglický originál a plná specifikace:** [AOC na 3GPP Explorer](https://3gpp-explorer.com/glossary/aoc/)
