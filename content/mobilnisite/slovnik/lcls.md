---
slug: "lcls"
url: "/mobilnisite/slovnik/lcls/"
type: "slovnik"
title: "LCLS – Local Call Local Switch"
date: 2025-01-01
abbr: "LCLS"
fullName: "Local Call Local Switch"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lcls/"
summary: "Funkce umožňující přímé přepínání datového provozu uživatelské roviny mezi dvěma uživatelskými zařízeními (UE) připojenými ke stejné základnové stanici nebo přístupovému bodu, s obcházením páteřní sít"
---

LCLS je funkce, která umožňuje přímé přepínání datového provozu uživatelské roviny mezi dvěma zařízeními připojenými ke stejné základnové stanici, s obcházením páteřní sítě za účelem snížení latence a zatížení.

## Popis

Local Call Local Switch (LCLS) je optimalizační funkce sítě definovaná ve standardech 3GPP, která umožňuje přímé směrování datového provozu uživatelské roviny mezi dvěma uživatelskými zařízeními (UE), když jsou připojena ke stejnému uzlu rádiového přístupu, jako je eNodeB v LTE nebo gNB v 5G NR. Hlavní architektonický princip spočívá v tom, že přístupový uzel provádí funkce místního přepínání, které tradičně zajišťovaly entity páteřní sítě, jako je Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v Evolved Packet Core (EPC) nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5G Core (5GC). Když dvě UE navážou komunikační relaci a jsou obě obsluhovány stejnou buňkou nebo společnou místní bránou, přístupový uzel tuto podmínku identifikuje a mezi UEs vytvoří přímý místní přenosový kanál (bearer). Tento místní kanál pro provoz mezi těmito dvěma koncovými body zcela obchází datovou cestu uživatelské roviny páteřní sítě.

Činnost LCLS je typicky spuštěna při vytváření nebo modifikaci vyhrazeného přenosového kanálu. Přístupový uzel ve spolupráci s řídicí rovinou páteřní sítě (např. [MME](/mobilnisite/slovnik/mme/) v EPC nebo [AMF](/mobilnisite/slovnik/amf/)/[SMF](/mobilnisite/slovnik/smf/) v 5GC) vyhodnotí umístění UEs. Pokud se zjistí, že se nacházejí v jeho servisní oblasti pro příslušné připojení Packet Data Network ([PDN](/mobilnisite/slovnik/pdn/)) nebo [PDU](/mobilnisite/slovnik/pdu/) Session, přístupový uzel nakonfiguruje svou vnitřní přepínací strukturu tak, aby směroval pakety přímo mezi odpovídajícími rádiovými přenosovými kanály obou UEs. Signalizace řídicí roviny (např. správa relací, správa mobility, účtování) stále prochází páteřní sítí, aby byla zachována správa účastníků, vynucování politik a možnosti zákonného odposlechu. Přístupový uzel může také na místně přepínané cestě zajišťovat potřebné vynucování kvality služeb (QoS) a označování paketů.

Klíčové komponenty umožňující LCLS zahrnují rozšířený uzel rádiového přístupu (např. eNodeB s funkcí LCLS), entity řídicí roviny páteřní sítě, které místní přepínání autorizují a nařizují, a v některých architekturách případně místní bránu (Local Gateway, L-GW) umístěnou společně s přístupovým uzlem. Její úlohou v síti je mechanismus pro přesměrování provozu a optimalizaci. Je obzvláště významná ve scénářích s vysokou hustotu místní komunikace, jako jsou stadiony, továrny nebo kampusy, kde zlepšuje výkon snížením celkové latence a kolísání zpoždění (jitteru) a zároveň šetří cenné zdroje přenosových tras (backhaul) a páteřní sítě.

## K čemu slouží

LCLS byla vytvořena, aby řešila neefektivitu směrování veškerého datového provozu uživatelské roviny přes centralizované brány páteřní sítě, zejména pro komunikaci mezi zařízeními, která jsou geograficky blízko a připojena ke stejnému přístupovému bodu. Před zavedením LCLS byl i provoz hovoru mezi dvěma telefony ve stejné budově potenciálně směrován stovky kilometrů do datového centra páteřní sítě a zpět, což způsobovalo zbytečnou latenci, spotřebovávalo kapacitu přenosových tras (backhaul) a zatěžovalo uzly páteřní sítě. Toto 'trombónové' nebo 'zpětné' směrování provozu je plýtvavé a škodlivé pro aplikace citlivé na výkon.

Historický kontext LCLS zahrnuje nárůst potřeb lokalizované komunikace s vysokou hustotou a snahu o efektivitu sítě ve standardech 3GPP přibližně od Release 9. Podporuje širší cíle služeb založených na blízkosti (ProSe) a přesměrování provozu ze sítě. Řešením problému směrování místního provozu LCLS umožňuje místní služby s nízkou latencí, snižuje provozní náklady operátorům úsporou přenosových zdrojů a zlepšuje celkovou škálovatelnost sítě pro scénáře komunikace typu stroj-stroj (MTC) a internetu věcí (IoT), kde zařízení v místní oblasti často komunikují mezi sebou.

LCLS dále položila základy pro pozdější vylepšení v oblasti mobilních výpočtů na okraji sítě (edge computing) a architektur místního průniku provozu (local breakout). Řeší omezení čistě centralizovaného modelu páteřní sítě distribucí přepínací inteligence na okraj sítě, což je v souladu s trendy směrem k decentralizovaným a cloud-nativním síťovým architekturám v pozdějších releasech 5G.

## Klíčové vlastnosti

- Přímé vytváření datové cesty uživatelské roviny mezi UEs na uzlu rádiového přístupu
- Obchází brány páteřní sítě (SGW/PGW, UPF) pro místní provoz
- Snižuje celkovou latenci (end-to-end) a kolísání zpoždění paketů (jitter)
- Šetří kapacitu přenosových tras (backhaul) a přenosovou šířku pásma páteřní sítě
- Zachovává řídicí rovinu páteřní sítě pro signalizaci, politiky a účtování
- Aplikovatelná pro architektury LTE/EPC i 5G NR/5GC

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [eNB – Evolved Node B](/mobilnisite/slovnik/enb/)
- [MEC – Multi-Access Edge Computing](/mobilnisite/slovnik/mec/)

## Definující specifikace

- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 23.284** (Rel-19) — Local Call Local Switch Stage 2
- **TS 23.889** (Rel-10) — Local Call Local Switch Core Network Impact Study
- **TS 29.205** (Rel-19) — BICC Protocols for Bearer-Independent CS Core Network
- **TS 48.008** (Rel-19) — BSS-MSC Interface Layer 3 Procedures

---

📖 **Anglický originál a plná specifikace:** [LCLS na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcls/)
