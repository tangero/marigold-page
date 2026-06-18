---
slug: "dsma-cd"
url: "/mobilnisite/slovnik/dsma-cd/"
type: "slovnik"
title: "DSMA-CD – Digital Sense Multiple Access - Collision Detection"
date: 2025-01-01
abbr: "DSMA-CD"
fullName: "Digital Sense Multiple Access - Collision Detection"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dsma-cd/"
summary: "DSMA-CD je metoda přístupu k rádiovému kanálu používaná v raných vydáních 3GPP UMTS pro náhodný přístup v uplinku. Kombinuje digitální snímání a detekci kolizí pro řízení přenosů od více uživatelských"
---

DSMA-CD je metoda přístupu k rádiovému kanálu používaná v raných vydáních 3GPP UMTS pro náhodný přístup v uplinku, která kombinuje digitální snímání (digital sensing) a detekci kolizí pro řízení přenosů od více uživatelských zařízení.

## Popis

Digital Sense [Multiple Access](/mobilnisite/slovnik/multiple-access/) with Collision Detection (DSMA-CD) je protokol řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) specifikovaný v 3GPP pro [UTRAN](/mobilnisite/slovnik/utran/) (UMTS terrestrial radio access network). Funguje na fyzické a MAC vrstvě a koordinuje uplinkové přenosy z více uživatelských zařízení (UE) k Node B (základnové stanici). Protokol je navržen pro kanály náhodného přístupu ([RACH](/mobilnisite/slovnik/rach/)), kde se UE pokoušejí odesílat data nebo řídicí informace bez předchozího naplánování. DSMA-CD funguje tak, že UE nejprve digitálně snímá aktivitu na kanále před vysíláním; pokud je kanál volný, zahájí přenos, ale pokud je detekována kolize (např. prostřednictvím zpětné vazby z Node B), použije algoritmus backoff a opakuje pokus po náhodném zpoždění. Tento hybridní přístup kombinuje prvky metody CSMA (Carrier Sense Multiple Access) a mechanismů detekce kolizí za účelem optimalizace využití kanálu.

Klíčové součásti DSMA-CD zahrnují vysílač a přijímač UE pro snímání, obvody pro detekci kolizí v Node B a signalizaci zpětné vazby přes downlinkové řídicí kanály. Když chce UE získat přístup k uplinku, nejprve naslouchá pilotnímu signálu nebo signálu obsazenosti (busy tone) vysílanému Node B, aby zjistilo, zda je kanál volný. Po zahájení přenosu Node B monitoruje překrývající se signály z více UE; pokud dojde ke kolizi, odešle záporné potvrzení nebo specifický indikátor kolize, což přiměje UE přenos přerušit a opakovat. Protokol používá digitální zpracování místo analogického snímání, což umožňuje přesnější detekci v hlučném rádiovém prostředí celulárních systémů. Jeho úlohou je minimalizovat kolize paketů, snížit latenci a zvýšit efektivitu sdílených rádiových zdrojů, zejména ve scénářích s nepravidelným provozem, jako je signalizace nebo přenosy malých datových dávek.

V praxi je DSMA-CD implementován v rámci specifikací fyzické vrstvy UMTS, jako je TS 25.211, která detailně popisuje rámcovou strukturu a kódování kanálu. Interaguje s protokoly vyšších vrstev, jako je [RLC](/mobilnisite/slovnik/rlc/) (Radio Link Control) a [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control), pro řízení pokusů o přístup a přidělování zdrojů. Tato technologie je klíčová pro zvládání přístupu založeného na soutěžení (contention-based) v uplinku a podporuje aplikace od počátečního připojení k síti až po občasné přenosy dat. Zatímco pozdější vydání 3GPP směřovala k více naplánovaným metodám přístupu, jako v LTE, DSMA-CD představoval důležitý krok v optimalizaci náhodného přístupu pro rané sítě 3G, vyvažující jednoduchost a výkon v dynamickém uživatelském prostředí.

## K čemu slouží

DSMA-CD byl vyvinut, aby řešil výzvu efektivního víceuživatelského přístupu v uplinku sítí UMTS, kde více UE soutěží o sdílené rádiové zdroje bez centralizovaného plánování. Před jeho zavedením se používaly jednodušší metody náhodného přístupu, jako je slotted ALOHA, které trpěly vysokou mírou kolizí a nízkou propustností, zejména s rostoucí hustotou uživatelů. DSMA-CD zavedl digitální snímání a detekci kolizí ke snížení kolizí a zlepšení využití kanálu, čímž řešil problémy s interferencí a zpožděním v raných systémech 3G.

Historicky se DSMA-CD objevil ve 3GPP Release 4 jako součást vylepšení fyzické vrstvy [UTRAN](/mobilnisite/slovnik/utran/), motivovaný potřebou lepšího výkonu paketových služeb a signalizace. Navazoval na koncepty z protokolů pro drátové sítě [LAN](/mobilnisite/slovnik/lan/), jako je CSMA/CD u Ethernetu, ale přizpůsobil je pro bezdrátová celulární prostředí, kde jsou podmínky na kanále proměnlivější a zpětnovazební smyčky delší. Protokol si kladl za cíl poskytnout rovnováhu mezi flexibilitou přístupu založeného na soutěžení a řízeným správou zdrojů, což umožnilo efektivní zpracování přerušovaného provozu typického pro mobilní komunikaci.

Zavedením DSMA-CD se 3GPP snažilo zlepšit uživatelský zážitek z datových aplikací a snížit režii spojenou s procedurami náhodného přístupu. Řešil omezení dřívějších přístupů začleněním digitálních detekčních mechanismů, které jsou méně náchylné k chybám než analogické snímání, a integrací s funkcemi řízení výkonu a časového předstihu v UMTS. To umožnilo spolehlivější uplinkové přenosy, podpořilo růst mobilních datových služeb na počátku roku 2000 a položilo základy pro pozdější pokroky v naplánovaném přístupu LTE.

## Klíčové vlastnosti

- Používá digitální snímání kanálu k detekci stavu volno/obsazeno před vysíláním UE
- Začleňuje detekci kolizí prostřednictvím zpětné vazby z Node B za účelem přerušení kolizních paketů
- Používá algoritmy náhodného backoff pro řešení kolizí a opakování pokusů o přístup
- Funguje na kanálech náhodného přístupu (RACH) UMTS pro soutěživý přístup v uplinku
- Integruje se s rámcovou strukturou a mechanismy řízení výkonu fyzické vrstvy UMTS
- Snižuje interferenci a zlepšuje propustnost ve sdílených rádiových prostředích

## Související pojmy

- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels

---

📖 **Anglický originál a plná specifikace:** [DSMA-CD na 3GPP Explorer](https://3gpp-explorer.com/glossary/dsma-cd/)
