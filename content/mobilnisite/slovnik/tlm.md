---
slug: "tlm"
url: "/mobilnisite/slovnik/tlm/"
type: "slovnik"
title: "TLM – TeLeMetry word"
date: 2025-01-01
abbr: "TLM"
fullName: "TeLeMetry word"
category: "Physical Layer"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/tlm/"
summary: "Specifické datové slovo používané v telemetrii pro 3GPP konformační testování rádiové frekvence (RF) uživatelského zařízení (UE). Obsahuje pevnou 8bitovou předmluvu (10001011) a slouží k ověření přesn"
---

TLM je standardizované telemetrické datové slovo obsahující pevnou 8bitovou předmluvu, používané v 3GPP RF konformačním testování pro ověření přesnosti modulace vysílače UE a výkonu přijímače.

## Popis

Telemetrické slovo (TLM) je základní součástí testovacích postupů fyzické vrstvy definovaných 3GPP pro uživatelská zařízení (UE). Není to protokol ani síťová funkce, ale specifická, předem daná bitová sekvence generovaná a zpracovávaná testovacími zařízeními pro vyhodnocení [RF](/mobilnisite/slovnik/rf/) výkonu vysílače a přijímače UE. Hlavní úlohou TLM slova je sloužit jako známý referenční signál, který umožňuje testovacím systémům měřit klíčové parametry, jako je velikost chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)), chyba frekvence a přesnost regulace výkonu během konformačního testování.

Při testování vysílače je UE instruováno, aby modulovalo a vysílalo souvislý proud TLM slov. Testovací zařízení tento RF signál zachytí, demoduluje jej a porovná přijatou bitovou sekvenci s očekávaným, známým TLM vzorem. Jakákoli odchylka je kvantifikována jako metriky kvality modulace. Pevná 8bitová předmluva (binárně 10001011) je kritickou součástí tohoto slova, neboť poskytuje předvídatelný vzor, který napomáhá synchronizaci signálu a analýze v algoritmech testovacího zařízení. Tato předmluva zajišťuje, že se testovací systém může přesně zachytit na signál a provádět konzistentní měření.

Pro testování přijímače testovací zařízení generuje standardní RF signál modulovaný sekvencí TLM slov a vysílá jej testovanému UE. Přijímač UE musí tento signál úspěšně demodulovat a dekódovat. Test poté měří citlivost přijímače UE, maximální vstupní úroveň a výkon za přítomnosti interference analýzou chybovosti bitů ([BER](/mobilnisite/slovnik/ber/)) nebo bloků ([BLER](/mobilnisite/slovnik/bler/)) na přijatých TLM datech. Použití standardizovaného, nerandomizovaného slova jako je TLM eliminuje variabilitu testovacího stimulu a zajišťuje, že všechna UE jsou testována vůči identické referenci, což je klíčové pro certifikaci a zaručení interoperability v reálných sítích.

Z architektonického hlediska existuje TLM slovo v rámci testovacích specifikací (TS 25.171 pro [UTRA](/mobilnisite/slovnik/utra/), TS 36.171 pro [E-UTRA](/mobilnisite/slovnik/e-utra/)) a je implementováno v softwaru a hardwaru akreditovaných konformačních testovacích systémů. Jedná se o nízkourovňový, statický datový vzor bez inteligence nebo konfigurovatelnosti. Jeho hodnota spočívá čistě v jeho předvídatelnosti, která je základním kamenem reprodukovatelného a srovnatelného testování RF výkonu. Ačkoli není součástí provozní síťové signalizace, důkladné testování umožněné nástroji jako je TLM slovo je nezbytné pro zajištění, že komerční zařízení splňují přísné požadavky na RF výkon stanovené 3GPP, což přímo ovlivňuje pokrytí sítě, její kapacitu a uživatelský zážitek.

## K čemu slouží

TLM slovo bylo vytvořeno za účelem poskytnutí standardizovaného, předvídatelného datového vzoru pro přesné a reprodukovatelné testování [RF](/mobilnisite/slovnik/rf/) výkonu UE. Před takovou standardizací se testovací metodologie mohly lišit mezi různými výrobci zařízení a testovacími domy, což vedlo k nekonzistentnostem v certifikaci zařízení a potenciálním problémům s interoperabilitou v nasazených sítích. TLM slovo tento problém řeší definicí univerzální 'testovací věty', kterou používají všechny strany, a zajišťuje, že přesnost modulace a citlivost přijímače UE jsou měřeny za identických podmínek bez ohledu na to, kde nebo kdy je test proveden.

Jeho zavedení v 3GPP Release 6 spolu s podrobnými specifikacemi pro RF konformační testování bylo motivováno rostoucí složitostí [WCDMA](/mobilnisite/slovnik/wcdma/) (UMTS) a potřebou důkladnějšího zajištění kvality s rozvojem mobilních datových služeb. Přesný RF výkon je zásadní pro spektrální účinnost, kapacitu sítě a životnost baterie. Zařízení s nízkou kvalitou modulace vytváří zbytečný interference pro ostatní uživatele a degraduje celkový výkon sítě. TLM slovo jako součást komplexní testovací sady umožňuje výrobcům identifikovat a opravit takové problémy během vývoje a poskytuje regulatorním orgánům a operátorům jistotu v kvalitu zařízení před uvedením na trh.

Pevná předmluva v rámci TLM slova konkrétně řeší potřebu spolehlivé akvizice a synchronizace signálu v testovacím zařízení. V hlučném testovacím prostředí se musí zařízení rychle a přesně zachytit na signál vysílaný UE, aby mohlo začít měření. Zvolený vzor předmluvy (10001011) nabízí dobré autokorelační vlastnosti, což usnadňuje algoritmům testovacího systému detekovat začátek rámce TLM slova ve signálu, a tím zlepšuje rychlost a spolehlivost provádění testu. Tento důraz na efektivitu testování je klíčový pro certifikaci velkého množství zařízení.

## Klíčové vlastnosti

- Pevná 8bitová předmluva (10001011) pro spolehlivou synchronizaci signálu
- Standardizovaná bitová sekvence pro konzistentní 3GPP RF konformační testování UE
- Používá se pro vyhodnocení přesnosti modulace vysílače (např. EVM)
- Používá se pro vyhodnocení výkonu přijímače (např. citlivost, BER)
- Definováno v 3GPP testovacích specifikacích (TS 25.171, TS 36.171)
- Umožňuje reprodukovatelná a srovnatelná měření napříč testovacími laboratořemi

## Související pojmy

- [EUTRA – Evolved Universal Terrestrial Radio Access](/mobilnisite/slovnik/eutra/)
- [UTRA – Universal Terrestrial Radio Access](/mobilnisite/slovnik/utra/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE

---

📖 **Anglický originál a plná specifikace:** [TLM na 3GPP Explorer](https://3gpp-explorer.com/glossary/tlm/)
