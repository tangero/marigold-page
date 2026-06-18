---
slug: "sci"
url: "/mobilnisite/slovnik/sci/"
type: "slovnik"
title: "SCI – Subscriber Controlled Input / Send Charging Information"
date: 2025-01-01
abbr: "SCI"
fullName: "Subscriber Controlled Input / Send Charging Information"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sci/"
summary: "SCI odkazuje na dva odlišné 3GPP koncepty. Primárně se jedná o servisní funkci umožňující účastníkům ovládat doplňkové služby pomocí pásmových DTMF tónů. Označuje také 'Send Charging Information', atr"
---

SCI je 3GPP termín, který primárně označuje servisní funkci umožňující účastníkům ovládat doplňkové služby pomocí DTMF tónů, a také označuje atribut protokolu 'Send Charging Information' pro předávání fakturačních dat.

## Popis

SCI v terminologii 3GPP zahrnuje dvě hlavní definice, obě související s řízením služeb, ale v různých doménách. První a historicky starší význam je 'Subscriber Controlled Input' (vstup řízený účastníkem). Jedná se o servisní schopnost v architektuře služeb přepojování okruhů. Umožňuje účastníkovi během aktivního hovoru interagovat s síťovými doplňkovými službami (jako je přesměrování hovoru, zákaz hovoru) a řídit je. Tato interakce se provádí pomocí pásmových [DTMF](/mobilnisite/slovnik/dtmf/) (Dual-Tone Multi-Frequency) tónů. Síť poskytuje hlášení nebo výzvy a uživatel reaguje stisknutím tlačítek na svém telefonu, čímž generuje DTMF signály, které jsou detekovány a interpretovány servisní logikou sítě.

Technická implementace zahrnuje detekci DTMF číslic během hovoru funkcí Service Switching Function ([SSF](/mobilnisite/slovnik/ssf/)) v [MSC](/mobilnisite/slovnik/msc/). Tyto číslice jsou zabaleny a předány funkci Service Control Function ([SCF](/mobilnisite/slovnik/scf/)), která typicky sídlí na platformě služeb [CAMEL](/mobilnisite/slovnik/camel/) nebo [IN](/mobilnisite/slovnik/in/). SCF obsahuje servisní logiku, která vstup interpretuje a provede odpovídající akci, jako je aktivace přesměrování hovoru nebo zadání nového hesla. Tento mechanismus poskytuje uživatelsky přívětivé, reálné rozhraní pro správu služeb bez nutnosti ukončit hovor nebo použít samostatné signalizační procedury.

Druhý hlavní význam SCI je 'Send Charging Information' (odeslání účtovacích informací). Jedná se o kritický atribut v rámci protokolu Diameter, konkrétně používaný na referenčních bodech Ro a Gy pro interakce s Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)). Když síťový prvek (jako [P-GW](/mobilnisite/slovnik/p-gw/) nebo S-CSCF) žádá o kvótu pro servisní relaci od OCS, zahrne atribut SCI ve zprávě Credit-Control-Request (CCR). Hodnota atributu SCI instruuje OCS, zda má vrátit účtovací informace, jako je cena servisní jednotky, v následující zprávě Credit-Control-Answer (CCA).

Tento účtování související SCI je příznak, který síti umožňuje poskytovat koncovému uživateli informace o účtování v reálném čase. Například v relaci předplacených dat může P-GW nastavit SCI tak, aby požádal OCS o odeslání ceny za megabajt. OCS tuto informaci zahrne do své odpovědi a P-GW nebo samostatný aplikační server ji pak může naformátovat a prezentovat účastníkovi prostřednictvím SMS nebo USSD zprávy. Tato funkce je klíčová pro transparentnost předplacených služeb a je vyžadována mnoha regulačními prostředími.

## K čemu slouží

Funkce 'Subscriber Controlled Input' (vstup řízený účastníkem) byla vytvořena za účelem zvýšení použitelnosti a flexibility doplňkových služeb založených na inteligentní síti (IN) a CAMEL. Před existencí takových funkcí konfigurace služeb často vyžadovala vytočení specifických kódů před uskutečněním hovoru nebo interakci se zákaznickým servisem. SCI umožnila řízení během hovoru, což umožnilo scénáře jako aktivace přesměrování hovoru na základě stavu obsazenosti volaného bez zavěšení. Řešila potřebu dynamické, uživatelem řízené interakce se službami, čímž zpřístupnila pokročilé telefonní funkce a učinila je praktičtějšími.

Atribut 'Send Charging Information' (odeslání účtovacích informací) byl motivován rozvojem předplacených služeb a regulačními požadavky na transparentnost účtování. Když mobilní operátoři přešli za jednoduché postpaid účtování, potřebovali mechanismus pro kontrolu nákladů v reálném čase a upozorňování uživatelů. Atribut SCI v rámci účtovacího protokolu Diameter standardizoval způsob, jakým síťový prvek může vyžádat informace o ceně z účtovacího systému. Tím vyřešil problém neprůhledných předplacených zůstatků, kdy mohly uživatele překvapit odečtené částky. Poskytnutím standardizovaného způsobu získání a zobrazení cenových informací zlepšil zákaznický zážitek a pomohl operátorům dodržovat předpisy na ochranu spotřebitele. Jeho vytvoření bylo nedílnou součástí úspěchu komplexních předplacených datových a obsahových služeb.

## Klíčové vlastnosti

- (Subscriber Controlled Input) Umožňuje řízení doplňkových služeb v reálném čase pomocí DTMF tónů
- (Subscriber Controlled Input) Usnadňuje interakci mezi uživatelem a servisní logikou IN/CAMEL během hovoru
- (Send Charging Information) Atribut (AVP) protokolu Diameter používaný na rozhraních Ro a Gy
- (Send Charging Information) Příznak žádosti, aby OCS vrátil účtovací/cenové informace
- Podporuje scénáře řízení služeb v přepojování okruhů i online účtování v přepojování paketů
- Zlepšuje uživatelský zážitek prostřednictvím interaktivního řízení služeb a transparentnosti účtování

## Související pojmy

- [DTMF – Dual Tone Multiple Frequency](/mobilnisite/slovnik/dtmf/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [IN – Intelligent Network](/mobilnisite/slovnik/in/)
- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [CCR – Credit-Control-Request](/mobilnisite/slovnik/ccr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study
- **TS 43.033** (Rel-13) — Lawful Interception Stage 2 for GSM/GPRS

---

📖 **Anglický originál a plná specifikace:** [SCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sci/)
