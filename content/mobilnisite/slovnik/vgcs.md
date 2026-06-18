---
slug: "vgcs"
url: "/mobilnisite/slovnik/vgcs/"
type: "slovnik"
title: "VGCS – Voice Group Call Service"
date: 2025-01-01
abbr: "VGCS"
fullName: "Voice Group Call Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vgcs/"
summary: "VGCS je služba 3GPP umožňující poloduplexní skupinové hlasové hovory, kdy jeden uživatel může mluvit k mnoha posluchačům najednou. Je klíčová pro komunikaci v oblasti veřejné bezpečnosti, dopravy a po"
---

VGCS je služba 3GPP umožňující poloduplexní skupinové hlasové hovory, při nichž jeden uživatel mluví k mnoha posluchačům najednou; používá se pro komunikaci v oblasti veřejné bezpečnosti, dopravy a dispečerské komunikace podniků.

## Popis

Služba skupinového hovoru (Voice Group Call Service, VGCS) je standardizovaná služba 3GPP, která umožňuje poloduplexní skupinovou hlasovou komunikaci, při níž jeden účastník (mluvčí) může vysílat současně k více posluchačům v rámci definované skupiny. Z architektonického hlediska VGCS využívá stávající infrastrukturu sítí GSM nebo UMTS, ale zavádí specifické funkční entity a signalizační postupy pro správu skupinových hovorů. Mezi klíčové komponenty patří registr skupinových hovorů (Group Call Register, [GCR](/mobilnisite/slovnik/gcr/)), který ukládá konfigurace skupin a data účastníků, a ústředna mobilní sítě (Mobile Switching Center, [MSC](/mobilnisite/slovnik/msc/)), která zajišťuje sestavení hovoru a přepojování. Služba funguje tak, že v přístupové rádiové síti vytvoří sdílený kanál pro přenos dat ve směru k účastníkům (downlink) pro všechny členy skupiny v určité geografické oblasti, známé jako oblast skupinového hovoru (group call area), zatímco přenosový kanál ve směru od účastníka (uplink) je udělen výhradně aktuálnímu mluvčímu prostřednictvím mechanismu řízeného nebo soutěžního přístupu.

Sestavení VGCS hovoru je zahájeno členem skupiny nebo dispečerem, což spustí proces, kdy MSC načte data skupiny z GCR a přidělí potřebné rádiové zdroje. Síť vyvolá členy skupiny v cílové oblasti a po jejich odezvě naváže spojení typu point-to-multipoint. Kritickým aspektem je řízení uplinku: uživatelé požádají o slovo odesláním notifikace a síť právo mluvit udělí na základě priority nebo principu „kdo dřív přijde, ten dřív mele“, čímž zajišťuje, že v jednom okamžiku je aktivní pouze jeden uplink, aby nedocházelo ke kolizím. Toto je řízeno pomocí signalizace v pásmu (in-band) nebo vyhrazených řídicích kanálů. Služba podporuje jak předem definované statické skupiny, tak dynamické skupiny vytvořené ad-hoc, a obsahuje bezpečnostní prvky, jako je skupinová autentizace a šifrování pro ochranu komunikace.

VGCS je integrována se službami určování polohy pro definování oblastí skupinového hovoru, což může být jedna buňka, více buněk nebo oblast polohy, a tím optimalizuje využití zdrojů. Podporuje doplňkové služby, jako jsou nouzové skupinové hovory, vysílací hovory (kde posluchači se nemohou stát mluvčími) a stavové zprávy. Služba je definována tak, aby fungovala jak v okruhově přepínané doméně, tak (v pozdějších vydáních) v paketově přepínané doméně, ačkoli původně byla navržena pro GSM. Její role je klíčová v komunikaci pro plnění misí (mission-critical), neboť poskytuje spolehlivou skupinovou hlasovou komunikaci v široké oblasti bez nutnosti samostatných vyhrazených sítí, a tím využívá pokrytí komerčních mobilních sítí pro profesionální případy užití a případy užití v oblasti veřejné bezpečnosti.

## K čemu slouží

VGCS byla vytvořena, aby uspokojila potřebu efektivní skupinové komunikace přes veřejné mobilní sítě, zejména pro profesionální uživatele a uživatele vyžadující komunikaci pro plnění misí. Před její standardizací byly tyto potřeby uspokojovány systémy privátní mobilní rádiové sítě (Private Mobile Radio, PMR), jako je [TETRA](/mobilnisite/slovnik/tetra/), nebo proprietárními řešeními, která vyžadovala samostatnou infrastrukturu a zařízení, což vedlo k vyšším nákladům a omezenému pokrytí. VGCS měla za cíl využít všudypřítomné pokrytí sítí GSM k poskytnutí služeb skupinové hlasové komunikace v široké oblasti, což umožnilo organizacím, jako jsou složky veřejné bezpečnosti, dopravní společnosti a energetické společnosti, provádět dispečerskou a koordinační komunikaci bez nutnosti investovat do vyhrazených sítí.

Motivace vycházela z omezení stávajících hlasových služeb mobilních sítí, které byly primárně bod-bod (jeden k jednomu) nebo konferenční hovory s omezenou škálovatelností a efektivitou pro scénáře jeden k mnoha. Konferenční hovory spotřebovávají významné síťové zdroje na účastníka a postrádají řízené právo mluvit. VGCS zavedla poloduplexní model se sdíleným kanálem, který optimalizuje rádiové spektrum a kapacitu sítě tím, že umožňuje více uživatelům naslouchat na jednom downlink kanálu, čímž je škálovatelná pro velké skupiny. To bylo zvláště cenné ve scénářích, jako je reakce na mimořádné události, kde velitelé potřebují vysílat pokyny mnoha terénním pracovníkům současně.

Historicky byla VGCS součástí snah 3GPP o vylepšení GSM pro profesionální použití, čímž překlenula propast mezi komerčními mobilními sítěmi a systémy PMR. Řešila problémy s pokrytím, interoperabilitou a náklady, což uživatelům umožnilo využívat standardní mobilní telefony s podporou VGCS. Služba také podporovala regulatorní požadavky na komunikaci pro veřejnou bezpečnost a poskytovala funkce jako priorita přednostního přerušení a geografické omezení hovoru. Integrací funkce skupinového hovoru do hlavních standardů mobilních sítí VGCS usnadnila konvergenci komerční a kritické komunikace a připravila půdu pro pozdější vylepšení, jako je [MCPTT](/mobilnisite/slovnik/mcptt/) (Mission Critical Push-To-Talk) přes LTE.

## Klíčové vlastnosti

- Poloduplexní skupinová hlasová komunikace s jedním mluvčím a více posluchači
- Dynamická správa práva mluvit prostřednictvím síťově řízeného udělení uplinku
- Definice geografické oblasti skupinového hovoru pro optimalizované přidělování zdrojů
- Podpora předem definovaných statických skupin a ad-hoc vytvořených dynamických skupin
- Integrace s okruhově přepínanými a paketově přepínanými síťovými doménami
- Bezpečnostní prvky včetně skupinové autentizace a šifrování na rádiovém rozhraní

## Související pojmy

- [GCR – Global Call Reference](/mobilnisite/slovnik/gcr/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.067** (Rel-19) — Enhanced Multi-Level Precedence and Pre-emption Service
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.796** (Rel-16) — FRMCS Architectural Analysis
- **TS 24.067** (Rel-19) — eMLPP Supplementary Service Procedures
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 43.020** (Rel-19) — Security Procedures for GSM
- **TS 43.068** (Rel-19) — Voice Group Call Service (VGCS) Stage 2
- **TS 43.069** (Rel-19) — Voice Broadcast Service (VBS) Stage 2
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TS 44.068** (Rel-19) — Group Call Control (GCC) Protocol for VGCS
- **TS 55.236** (Rel-19) — A8_V MILENAGE Algorithm for VGCS/VBS Security

---

📖 **Anglický originál a plná specifikace:** [VGCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/vgcs/)
