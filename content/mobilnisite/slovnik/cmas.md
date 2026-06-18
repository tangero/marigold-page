---
slug: "cmas"
url: "/mobilnisite/slovnik/cmas/"
type: "slovnik"
title: "CMAS – Commercial Mobile Alert Service"
date: 2026-01-01
abbr: "CMAS"
fullName: "Commercial Mobile Alert Service"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cmas/"
summary: "CMAS je standardizovaný systém veřejného varování podle 3GPP, který doručuje nouzové výstrahy (např. extrémní počasí, AMBER výstrahy) mobilním uživatelům prostřednictvím celulárního vysílání (broadcas"
---

CMAS je standardizovaný systém veřejného varování podle 3GPP, který doručuje geograficky cílené nouzové výstrahy mobilním uživatelům prostřednictvím celulárního vysílání (broadcastu), čímž zajišťuje rychlou komunikaci pro veřejnou bezpečnost bez zahlcení sítě.

## Popis

Commercial Mobile Alert Service (CMAS) je standardizovaná služba podle 3GPP pro doručování varovných zpráv veřejnosti na mobilní zařízení prostřednictvím mechanismů celulárního vysílání (broadcastu). Je navržena pro provoz na stávajících sítích 3GPP (od 3G výše) s využitím architektury Cell Broadcast Service ([CBS](/mobilnisite/slovnik/cbs/)). CMAS využívá stávající entity Broadcast/Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) a Cell Broadcast Center ([CBC](/mobilnisite/slovnik/cbc/)) pro šíření výstrah. BM-SC přijímá varovné zprávy od autorizovaných vládních agentur, zpracuje je a přepošle do CBC. CBC následně namapuje tyto výstrahy na příslušné geografické oblasti (buňky) a doručí je do rádiové přístupové sítě (RAN) pro vysílání. V RAN jsou výstrahy přenášeny přes rozhraní vzduch (air interface) pomocí bloků systémových informací ([SIB](/mobilnisite/slovnik/sib/)) v LTE nebo zpráv systémových informací ([SI](/mobilnisite/slovnik/si/)) v 5G NR, konkrétně prostřednictvím SIB12 v LTE a SIB6/SIB8 v 5G NR pro systém varování před zemětřesením a tsunami (ETWS) a výstrahy CMAS.

Zprávy CMAS jsou vysílány (broadcastovány) na všechna zařízení v cílové buňce nebo skupině buněk, což zajišťuje simultánní doručení bez režie signalizace typu point-to-point. Zařízení musí být CMAS-kompatibilní a nakonfigurovaná pro příjem takových výstrah. Po přijetí CMAS vysílání kompatibilní zařízení přeruší probíhající uživatelské aktivity (např. charakteristickým zvukem a vibracemi), aby zobrazila text výstrahy. Služba podporuje priorizaci zpráv s různými kategoriemi výstrah, jako jsou Prezidentské, Extrémní, Závažné, AMBER a Testovací výstrahy, přičemž každá má specifické požadavky na zpracování. Obsah zprávy zahrnuje typ varování, závažnost, naléhavost, jistotu a doporučené akce, formátované podle standardu Common Alerting Protocol ([CAP](/mobilnisite/slovnik/cap/)).

Mezi klíčové síťové komponenty patří Cell Broadcast Entity ([CBE](/mobilnisite/slovnik/cbe/)), která vytváří výstrahy od orgánů veřejné bezpečnosti, CBC pro geografické cílení a distribuci zpráv a BM-SC pro správu vysílacích relací v LTE/5G. V jádru sítě (core network) rozhraní CBC komunikuje s Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v LTE nebo s funkcí Access and Mobility Management Function (AMF) v 5G Core přes rozhraní SBc. RAN následně vysílá výstrahu pomocí signalizace RRC. CMAS zajišťuje spolehlivé doručení i v přetížených sítích díky využití vysílacích kanálů, čímž se vyhýbá problémům systémů založených na SMS. Také podporuje vícejazyčné výstrahy a geografické cílení až na úroveň buňky, což umožňuje přesné šíření varování. Služba je integrována s dalšími varovnými systémy, jako je ETWS, se kterým sdílí podobné vysílací mechanismy, ale liší se typy zpráv a jejich původem.

## K čemu slouží

CMAS byl vytvořen, aby řešil kritickou potřebu spolehlivého, rychlého a škálovatelného systému veřejného varování přes mobilní sítě. Před CMAS byly nouzové výstrahy často doručovány prostřednictvím TV, rádia nebo SMS, což mělo omezení v rychlosti, dosahu a cílení. Výstrahy založené na SMS mohly například způsobit zahlcení sítě a zpoždění kvůli point-to-point doručování a selhat při mimořádných událostech s vysokým provozem. CMAS využívá technologii celulárního vysílání (broadcastu) k překonání těchto problémů a umožňuje simultánní doručení na všechna zařízení v ohrožené oblasti bez přetížení sítě.

Vývoj CMAS byl motivován regulatorními požadavky a iniciativami veřejné bezpečnosti, zejména ve Spojených státech, kde zákon Warning, Alert, and Response Network (WARN) Act takovou službu vyžadoval. 3GPP standardizovalo CMAS počínaje Release 9, aby zajistilo globální interoperabilitu napříč sítěmi a zařízeními. Řeší problém včasné a přesné nouzové komunikace a poskytuje orgánům nástroj k varování veřejnosti před hrozícími nebezpečími, jako jsou přírodní katastrofy, teroristické útoky nebo únosy dětí (AMBER výstrahy). Využitím stávající celulární infrastruktury nabízí CMAS nákladově efektivní a široce dostupné řešení.

CMAS také řeší omezení dřívějších varovných systémů podporou geografického cílení, které zajišťuje, že výstrahy jsou odesílány pouze do postižených oblastí, a snižuje tak zbytečný poplach veřejnosti. Integruje se s mezinárodními standardy, jako je CAP, což umožňuje kompatibilitu s dalšími varovnými systémy. Služba zvyšuje veřejnou bezpečnost doručováním výstrah ve více jazycích a s odlišnými vizuálními/zvukovými signály, což zajišťuje, že si jich uživatelé všimnou i v hlučném prostředí. Celkově CMAS představuje významný pokrok v nouzové komunikaci, který využívá mobilní technologii k záchraně životů a zlepšení odolnosti komunity.

## Klíčové vlastnosti

- Doručování založené na vysílání (broadcastu) prostřednictvím služby Cell Broadcast Service (CBS) pro výstrahy šetrné k síti
- Geografické cílení až na úroveň buňky pro přesné šíření varování
- Podpora více kategorií výstrah (Prezidentské, Extrémní, Závažné, AMBER, Testovací)
- Integrace s Common Alerting Protocol (CAP) pro standardizované formátování zpráv
- Zpracování priorit a odlišná upozornění zařízení (zvuk, vibrace) pro zajištění pozornosti uživatele
- Vícejazyčná podpora a kompatibilita s dalšími varovnými systémy, jako je ETWS

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.268** (Rel-20) — Public Warning System (PWS) Requirements
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.168** (Rel-19) — SBc-AP Protocol Specification
- **TR 33.969** (Rel-19) — Security for Public Warning System (PWS)
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 36.410** (Rel-19) — S1 Interface: General Aspects and Principles
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [CMAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cmas/)
