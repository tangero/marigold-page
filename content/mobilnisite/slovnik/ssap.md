---
slug: "ssap"
url: "/mobilnisite/slovnik/ssap/"
type: "slovnik"
title: "SSAP – Supplementary Service Application Part"
date: 2025-01-01
abbr: "SSAP"
fullName: "Supplementary Service Application Part"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ssap/"
summary: "SSAP je signalizační protokol v rámci 3GPP Core Network, konkrétně součást architektury CAMEL (Customised Applications for Mobile network Enhanced Logic). Umožňuje řízení a správu doplňkových služeb,"
---

SSAP je signalizační protokol CAMEL v rámci 3GPP Core Network, který umožňuje komunikaci mezi síťovými entitami za účelem řízení doplňkových služeb, jako je přesměrování či zákaz hovorů.

## Popis

Supplementary Service Application Part (SSAP) je protokol definovaný ve specifikaci 3GPP TS 29.013, který funguje jako součást rámce Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) a [CAMEL](/mobilnisite/slovnik/camel/). Působí jako aplikační protokol, který pro spolehlivý přenos zpráv využívá Transaction Capabilities Application Part ([TCAP](/mobilnisite/slovnik/tcap/)) a Signaling Connection Control Part ([SCCP](/mobilnisite/slovnik/sccp/)) přes [SS7](/mobilnisite/slovnik/ss7/) nebo IP-based signalizační sítě. SSAP definuje zprávy a procedury pro interakci mezi gsmSCF (GSM Service Control Function) a [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre) nebo [SGSN](/mobilnisite/slovnik/sgsn/) (Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node). Tato interakce umožňuje gsmSCF, který hostuje servisní logiku pro doplňkové služby, řídit zpracování hovorů a relací v reálném čase. Například když účastník aktivuje přesměrování hovoru, může MSC vyvolat pomocí SSAP zpráv CAMEL dialog s gsmSCF, aby provedl konkrétní logiku přesměrování, jako je dotaz na data účastníka nebo aplikace časově závislých pravidel.

Architektonicky je SSAP servisně specifická adaptační vrstva umístěná nad TCAP. Definuje sadu operací a souvisejících parametrů, které modelují řízení doplňkových služeb. Tyto operace zahrnují požadavky od MSC směrem k gsmSCF (např. nahlášení události, jako je zahájení hovoru) a instrukce od gsmSCF zpět k MSC (např. připojit hovor na jiné číslo nebo přehrát oznámení). Protokol zajišťuje, že servisní logika v gsmSCF může ovlivňovat zpracování hovoru v ústředně bez nutnosti přímé integrace, což umožňuje jasné oddělení funkcí řízení služeb a přepojování. Toto oddělení je základním kamenem konceptu Inteligentní sítě a podporuje flexibilitu a rychlejší nasazování služeb.

Klíčové komponenty SSAP zahrnují jeho operační kódy, chybové kódy a struktury parametrů definované v ASN.1. Protokol řeší různé scénáře doplňkových služeb, včetně přesměrování hovorů (CFU, CFB, CFNRy, CFNRc), zákazu hovorů (BAOC, BOIC, BIC-Roam) a informování o ceně. Funguje ve spojení s dalšími CAMEL protokoly, jako je CAP (CAMEL Application Part) pro základní řízení hovorů a INAP pro interakce v pevných sítích. Zatímco CAP je široce používán pro řízení služeb v reálném čase, jako je předplacené účtování, SSAP je specificky navržen pro správu tradičních telefonních doplňkových služeb v obvodu přepínané doméně GSM/UMTS. Jeho fungování je úzce provázáno s profilem účastníka v HLR, který udává, které doplňkové služby jsou aktivní a zda je vyžadováno CAMEL řízení.

## K čemu slouží

SSAP byl vytvořen pro uspokojení potřeby standardizovaného, nezávislého řízení doplňkových služeb v mobilních sítích, zejména jako součást standardu CAMEL zavedeného ve fázi GSM Phase 2+. Před CAMEL a SSAP byly doplňkové služby, jako je přesměrování hovorů, implementovány pomocí proprietární logiky specifické pro daného dodavatele ústředen uvnitř MSC. To operátorům ztěžovalo rychlé zavádění nových služeb nebo zajištění konzistentního chování v síti s více dodavateli. Koncept Inteligentní sítě (IN), přijatý 3GPP jako CAMEL, si kladl za cíl oddělit servisní logiku od přepojovací hardwaru, což umožnilo vyvíjet a hostovat služby na centralizovaných platformách (gsmSCF).

SSAP konkrétně řeší problém, jak může tato centralizovaná servisní logika komunikovat s MSC a řídit ji v rámci scénářů doplňkových služeb. Poskytuje standardizovaný protokol, takže operátor může nasadit gsmSCF od jednoho dodavatele pro řízení MSC od jiného dodavatele, což podporuje interoperabilitu a snižuje závislost na jediném dodavateli. To bylo zvláště důležité pro umožnění pokročilých, operátorsky specifických služeb (jako jsou vlastní pravidla přesměrování hovorů na základě denní doby nebo identity volajícího), které přesahují rámec základních standardizovaných doplňkových služeb.

Historicky SSAP zaplnil specifickou mezeru v širší CAMEL architektuře. Zatímco CAP řešil základní řízení hovorů pro služby jako předplacené, SSAP se věnoval tradičnějším telefonním funkcím. Jeho vytvoření bylo motivováno snahou rozšířit výhody IN – flexibilitu, rychlé vytváření služeb a centralizované řízení – na celou sadu doplňkových služeb, což zajistilo ucelený rámec pro všechny přidané telefonní funkce v 2G a 3G obvodu přepínaných sítích.

## Klíčové vlastnosti

- Standardizovaný protokol pro komunikaci gsmSCF s MSC/SGSN v oblasti doplňkových služeb
- Umožňuje řízení přesměrování, zákazu hovorů a dalších telefonních funkcí v reálném čase
- Pro spolehlivý transakční přenos signalizace využívá TCAP a SCCP
- Definuje konkrétní operace a parametry v ASN.1 pro přesné řízení služeb
- Podporuje architekturu CAMEL Inteligentní sítě pro oddělení servisní logiky
- Usnadňuje interoperabilitu mezi více dodavateli při nasazování doplňkových služeb

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [TCAP – Transaction Capabilities Application Part](/mobilnisite/slovnik/tcap/)
- [INAP – Intelligent Network Application Protocol](/mobilnisite/slovnik/inap/)

## Definující specifikace

- **TS 29.013** (Rel-19) — MAP-SSAP Interworking for CCBS Service

---

📖 **Anglický originál a plná specifikace:** [SSAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssap/)
