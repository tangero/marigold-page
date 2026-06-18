---
slug: "cwi"
url: "/mobilnisite/slovnik/cwi/"
type: "slovnik"
title: "CWI – Character Waiting Integer"
date: 2025-01-01
abbr: "CWI"
fullName: "Character Waiting Integer"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cwi/"
summary: "CWI je parametr používaný ve specifikacích 3GPP pro správu zpoždění při přenosu dat po znacích, zejména v legacy systémech. Definuje celočíselnou hodnotu, která určuje čekací periody nebo intervaly op"
---

CWI je parametr 3GPP, který definuje celočíselnou hodnotu pro správu čekacích period při přenosu dat po znacích, aby bylo zajištěno spolehlivé řízení toku v zastaralých protokolech.

## Popis

Character Waiting Integer (CWI) je specifický celočíselný parametr definovaný v technických specifikacích 3GPP, primárně dokumentovaný v TS 21.905. Funguje jako konfigurovatelná hodnota časovače nebo čítače používaná pro správu časových aspektů v protokolech pro přenos dat po znacích. V praktické implementaci CWI nastavuje práh pro čekací periody mezi přenosy znaků, pokusy o opakovaný přenos nebo synchronizační intervaly, což je klíčové pro prevenci ztráty dat, správu přetečení vyrovnávací paměti a zajištění řádného zpracování v síťových prvcích, které obsluhují sériové nebo znakově orientované datové toky. Parametr je typicky konfigurován v síťovém zařízení nebo protokolových zásobnících, aby se přizpůsobil různým síťovým podmínkám a požadavkům služeb.

Z architektonického hlediska CWI funguje na protokolové vrstvě, kde je nutné zpracování znak po znaku, často v rozhraních nebo legacy subsystémech, které nepoužívají rámování založené na paketech. Je integrován do stavových automatů komunikačních protokolů, kde ovlivňuje chování, jako je časování mezi znaky, čekání na potvrzení a mechanismy řízení toku. Mezi klíčové komponenty ovlivněné CWI patří protokolové časovače, čítače opakování a logika správy vyrovnávací paměti, které společně zajišťují, že přenos dat dodržuje časová omezení bez zahlcení přijímajících entit. Jeho role je zvláště výrazná ve scénářích zahrnujících signalizaci založenou na textu, telemetrii nebo starší datové služby, kde je synchronizace znaků nezbytná pro správnou interpretaci.

V síti CWI přispívá ke spolehlivosti a efektivitě tím, že poskytuje laditelný parametr, který mohou síťoví operátoři upravovat na základě empirických výkonnostních dat. Například v prostředích náchylných k chybám může být nastavena vyšší hodnota CWI, aby umožnila delší čekací periody pro příjem znaků, čímž se sníží pravděpodobnost předčasných timeoutů a zbytečných opakovaných přenosů. Naopak na stabilních vysokorychlostních spojích může nižší CWI minimalizovat latenci a zlepšit propustnost. Hodnota parametru je často vyjednávána nebo staticky konfigurována během nastavení sítě nebo aktivace služby, čímž se zajišťuje kompatibilita mezi různými síťovými prvky a dodržování cílů kvality služeb (QoS).

Technické fungování CWI zahrnuje sledování uběhlého času nebo počtu událostí mezi událostmi souvisejícími se znaky. Když protokolová entita odešle nebo očekává znak, použije CWI k určení, jak dlouho čekat, než podnikne nápravnou akci, jako je opakovaný přenos nebo signalizace chyby. Tento mechanismus pomáhá spravovat chvění, zpoždění šíření a rozdíly ve zpracování v heterogenních sítích. Zatímco jeho použití s přechodem na paketové protokoly, jako je IP, pokleslo, CWI zůstává relevantní pro specifická legacy rozhraní, testovací scénáře a režimy zpětné kompatibility v systémech 3GPP, čímž zajišťuje bezproblémový provoz napříč vyvíjejícími se generacemi sítí.

## K čemu slouží

CWI bylo zavedeno k řešení časovacích a synchronizačních výzev v komunikaci dat po znacích v raných sítích 3GPP. Před jeho standardizací vedly ad-hoc časovací mechanismy k problémům s interoperabilitou, poškození dat a neefektivnímu využití síťových zdrojů, když různí dodavatelé zařízení implementovali proprietární čekací intervaly. Vytvoření CWI poskytlo jednotný, standardizovaný celočíselný parametr, který mohl být konzistentně aplikován napříč síťovými prvky, čímž se vyřešily problémy související se ztrátou znaků, desynchronizací a nadměrnými opakovanými přenosy v protokolech závislých na sériových tocích znaků.

Historicky, jak se telekomunikační sítě vyvíjely z čistě okruhově přepínaného hlasu tak, aby zahrnovaly datové služby, vznikla potřeba spravovat jednoduché znakově orientované protokoly pro signalizaci, správu a základní přenos dat. CWI vzniklo jako součást snahy 3GPP formalizovat tyto řídicí parametry, aby bylo zajištěno spolehlivé fungování v prostředích s více dodavateli. Odstranilo omezení předchozích přístupů tím, že nabídlo konfigurovatelnou hodnotu založenou na celém čísle, která mohla být optimalizována pro různé síťové podmínky, na rozdíl od pevných časovačů, kterým chyběla flexibilita. To umožnilo síťovým operátorům jemně ladit výkon na základě kvality spojení, vzdálenosti a požadavků aplikace.

Motivace za CWI také pramenila z nutnosti zachovat zpětnou kompatibilitu se staršími systémy při přechodu na pokročilejší architektury založené na paketech. Definováním standardního čekacího celého čísla umožnilo 3GPP hladší integraci starších znakových rozhraní s novějšími síťovými komponentami, čímž se snížily náklady na migraci a výpadky služeb. CWI tedy sehrálo roli při zajišťování kontinuity a spolehlivosti během vývoje sítě, zejména v pomocných funkcích, jako je [OAM](/mobilnisite/slovnik/oam/) (Provoz, správa a údržba), kde znakové protokoly přetrvávaly.

## Klíčové vlastnosti

- Definuje celočíselnou hodnotu pro čekací periody při přenosu znaků
- Konfigurovatelný parametr přizpůsobitelný síťovým podmínkám
- Zvyšuje spolehlivost v tocích dat po znacích
- Podporuje synchronizaci v legacy protokolových rozhraních
- Snižuje ztrátu dat prostřednictvím řízených intervalů opakování
- Usnadňuje interoperabilitu napříč zařízeními od více dodavatelů

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [CWI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cwi/)
