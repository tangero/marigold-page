---
slug: "sm-cp"
url: "/mobilnisite/slovnik/sm-cp/"
type: "slovnik"
title: "SM-CP – Short Message Control Protocol"
date: 2025-01-01
abbr: "SM-CP"
fullName: "Short Message Control Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sm-cp/"
summary: "Protokol v rámci architektury CAMEL (Customised Applications for Mobile network Enhanced Logic), který umožňuje chytré síti řídit aplikační logiku služby SMS. Umožňuje CAMEL Service Environment (CSE)"
---

SM-CP je protokol CAMEL, který umožňuje chytré síti řídit aplikační logiku služby SMS pro přidané služby.

## Popis

Short Message Control Protocol (SM-CP) je specifický aplikační protokol definovaný v rámci standardů 3GPP [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile network Enhanced Logic). Funguje mezi CAMEL Service Environment ([CSE](/mobilnisite/slovnik/cse/)) – které hostí aplikační logiku chytré sítě – a síťovou entitou zpracovávající [SMS](/mobilnisite/slovnik/sms/), typicky Short Message Service Center ([SMSC](/mobilnisite/slovnik/smsc/)) nebo IP Short Message Gateway ([IP-SM-GW](/mobilnisite/slovnik/ip-sm-gw/)). SM-CP se používá výhradně pro scénáře Mobile Terminated ([MT](/mobilnisite/slovnik/mt/)) SMS pod kontrolou CAMEL. Jeho hlavní funkcí je umožnit CSE zasáhnout do procesu doručování SMS, čímž umožňuje služby jako screening SMS, účtování, úprava směrování a notifikace.

Z architektonického hlediska je SM-CP součástí sady protokolů CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)). Když se SMSC chystá doručit [MT-SMS](/mobilnisite/slovnik/mt-sms/) účastníkovi s CAMEL předplatným pro SMS, spustí dialog s CSE. To se provede odesláním úvodní SM-CP zprávy, jako je "ConnectSMS", do CSE. Tato zpráva obsahuje klíčové informace o SMS, včetně čísla volaného (příjemce), čísla volajícího (odesílatele) a adresy SMSC. CSE, které provádí svou aplikační logiku (např. gsmSCF), pak tyto informace může analyzovat a dát SMSC pokyny, jak postupovat. To činí odesláním zpět odpovědí na SM-CP operace, které mohou SMSC nařídit pokračovat v doručení, ukončit transakci (zablokovat SMS), upravit parametry jako cílovou adresu nebo informace o účtování, nebo požádat o oznámení konečného výsledku doručení.

Protokol funguje transakčně, na principu požadavek-odpověď. Mezi klíčové operace patří "ConnectSMS" (iniciace), "FurnishChargingInformation" (pro odeslání účtovacích údajů), "ReleaseSMS" (pro ukončení) a "EventReportSMS" (pro notifikace). Prostřednictvím nich může CSE implementovat komplexní služby. Například služba rodičovské kontroly může použít SM-CP k screeningu zpráv na základě odesílatele a blokování těch z neznámých čísel. Služba prémiového obsahu jej může použít k aplikaci specifických tarifů před pokusem o doručení. Protokol zajišťuje, že aplikační logika chytré sítě je bezproblémově integrována do cesty doručení SMS, aniž by vyžadovala úpravy samotného jádra SMSC, čímž se drží filozofie CAMEL oddělující aplikační logiku od přepojovacích funkcí.

## K čemu slouží

SM-CP byl vytvořen, aby rozšířil možnosti konceptu Intelligent Network (IN) na službu Short Message Service. Před kontrolou CAMEL byla SMS základní přenosovou službou s omezenou síťovou kontrolou; služby jako screening nebo speciální účtování za SMS vyžadovaly proprietární funkce SMSC. SM-CP vyřešil problém aplikace standardizované, operátorem definované logiky na doručování SMS v reálném čase, což umožnilo novou třídu přidaných služeb.

Motivace vycházela z komerčního úspěchu SMS a touhy po dalším zpeněžení a kontroly. Operátoři chtěli nabízet služby jako SMS firewally, sponzorované zprávy nebo SMS směrování na základě polohy. Architektura CAMEL toto již poskytovala pro hovory (prostřednictvím CAP pro hovory) a SM-CP zaplnil mezeru pro doménu zasílání zpráv. Odstranil omezení "hloupého potrubí" pro doručování SMS tím, že poskytl standardizovaný bod pro spuštění aplikační logiky, což umožnilo vytváření služeb nezávisle na dodavatelích ústředen.

Historicky, zavedený v CAMEL Phase 3 (3GPP Release 5), umožnil SM-CP operátorům GSM a UMTS nasazovat konzistentní služby založené na SMS napříč jejich sítěmi. Umožnil stejné servisní platformě (CSE) řídit jak hlasové, tak zprávové služby, čímž zjednodušil provoz. Vytvoření protokolu bylo hnací silou potřeby flexibilní kontroly služeb, vylepšených modelů účtování pro prémiové SMS a regulatorních požadavků, jako je zákonné odposlouchávání SMS, a to vše v rámci standardizovaného rámce, který zajišťoval interoperabilitu mezi síťovými zařízeními různých výrobců.

## Klíčové vlastnosti

- Umožňuje CAMEL servisní kontrolu pro doručování Mobile Terminated SMS
- Definuje sadu CAP operací specifických pro SMS (např. ConnectSMS, ReleaseSMS)
- Umožňuje screening SMS, úpravu směrování a speciální účtování v reálném čase
- Podporuje hlášení událostí o stavu doručení SMS zpět do aplikační logiky
- Funguje mezi CAMEL Service Environment (CSE) a entitou zpracovávající SMS (např. SMSC)
- Umožňuje vytváření přidaných služeb SMS bez nutnosti úprav základních platforem SMSC

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)
- [SMSC – Short Message Service Centre](/mobilnisite/slovnik/smsc/)
- [MT-SMS – Mobile Terminated Short Message Service](/mobilnisite/slovnik/mt-sms/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification

---

📖 **Anglický originál a plná specifikace:** [SM-CP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sm-cp/)
