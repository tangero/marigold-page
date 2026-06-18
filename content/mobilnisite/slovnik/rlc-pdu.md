---
slug: "rlc-pdu"
url: "/mobilnisite/slovnik/rlc-pdu/"
type: "slovnik"
title: "RLC-PDU – Radio Link Control - Protocol Data Unit"
date: 2025-01-01
abbr: "RLC-PDU"
fullName: "Radio Link Control - Protocol Data Unit"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rlc-pdu/"
summary: "Datová jednotka vyměňovaná mezi podsložkou řízení rádiového spoje (Radio Link Control, RLC) a jejím protějškem. Jedná se o strukturovaný paket obsahující uživatelská data nebo řídicí informace, formát"
---

RLC-PDU je strukturovaná datová jednotka vyměňovaná mezi protějšky podsložky RLC, která obsahuje uživatelská data nebo řídicí informace formátované podle konkrétního režimu RLC pro spolehlivý přenos přes rozhraní rádiového spoje.

## Popis

RLC-PDU je základní datová jednotka zpracovávaná podsložkou řízení rádiového spoje (Radio Link Control, [RLC](/mobilnisite/slovnik/rlc/)), která je součástí vrstvy 2 (linkové vrstvy) v protokolovém zásobníku 3GPP pro uživatelskou i řídicí rovinu. Je to strukturovaný paket, který prochází rozhraním mezi entitou RLC a jejím protějškem na druhé straně rádiového spoje (např. z UE do gNB). Formát a obsah RLC-PDU jsou striktně definovány provozním režimem entity RLC: transparentní režim (Transparent Mode, [TM](/mobilnisite/slovnik/tm/)), nepotvrzovaný režim (Unacknowledged Mode, [UM](/mobilnisite/slovnik/um/)) nebo potvrzovaný režim (Acknowledged Mode, [AM](/mobilnisite/slovnik/am/)). V TM je RLC-PDU v podstatě služební datová jednotka (Service Data Unit, [SDU](/mobilnisite/slovnik/sdu/)) procházející bez přidání hlavičky, používaná pro zpoždění citlivé signalizace, jako je vysílání systémových informací. V UM a AM entita RLC přidává k SDU protokolovou hlavičku a vytváří tak [PDU](/mobilnisite/slovnik/pdu/). Tato hlavička obsahuje klíčové informace, jako je pořadové číslo (Sequence Number, [SN](/mobilnisite/slovnik/sn/)) pro doručování ve správném pořadí, indikátory segmentace a v AM také pole pro hlášení stavu ([ACK](/mobilnisite/slovnik/ack/)/NACK) na podporu automatického opakovaného dotazu (Automatic Repeat Request, ARQ) pro opravu chyb.

Vytváření RLC-PDU zahrnuje funkce jako segmentaci a/nebo konkatenaci RLC SDU (které přicházejí z horní vrstvy PDCP), aby se přizpůsobily velikosti přenosového bloku přiděleného spodní vrstvou MAC. Entita RLC přijímá RLC SDU a může velké SDU segmentovat do více RLC-PDU nebo několik malých SDU zřetězit do jediného RLC-PDU, čímž optimalizuje využití rádiových prostředků. Poté je připojena hlavička a kompletní RLC-PDU je předáno vrstvě MAC jako MAC SDU. Na přijímací straně protějšková entita RLC provádí zpětné operace: využívá informace v hlavičce k opětovnému sestavení původních RLC SDU z přijatých RLC-PDU, k jejich doručení ve správném pořadí do PDCP a v AM k odesílání hlášení stavu zpět vysílači, aby vyžádala retransmisi chybějících PDU.

Její role je klíčová pro poskytování služby přenosu dat požadované horními vrstvami. Pro signalizaci řídicí roviny (např. zprávy RRC) zajišťuje RLC v AM nebo TM spolehlivé nebo včasné doručení. Pro data uživatelské roviny je režim konfigurován pro každý datový rádiový bearer tak, aby odpovídal požadavkům QoS – UM pro služby citlivé na zpoždění, jako je VoIP (tolerující určitou ztrátu), a AM pro data netolerující chyby, jako je stahování souborů. RLC-PDU je tedy nástrojem pro implementaci klíčových funkcí RLC: opravy chyb prostřednictvím ARQ (v AM), doručování ve správném pořadí, detekce duplicit a řízení toku mezi vrstvami RLC a PDCP. Účinnost a spolehlivost celého toku dat přes rádiové rozhraní závisí na robustním návrhu a zpracování RLC-PDU.

## K čemu slouží

RLC-PDU existuje, aby poskytl standardizovaný, strukturovaný formát pro výměnu dat přes náchylný k chybám rádiový spoj, což umožňuje protokolu řízení rádiového spoje (RLC) plnit svůj úkol spolehlivého přenosu dat. Rádiový kanál je ze své podstaty nespolehlivý kvůli útlumu, interferencím a mobilitě, což vede ke zkreslení nebo ztrátě datových paketů. Pouhé předávání nezpracovaných datových paketů (SDU) z horní vrstvy PDCP do spodní vrstvy MAC by nestačilo k zaručení kvality služby požadované různorodými aplikacemi. RLC-PDU se svou režimově specifickou hlavičkou je mechanismus, který umožňuje vrstvě RLC přidat k každé datové jednotce potřebné řídicí informace (jako jsou pořadová čísla). Tyto řídicí informace umožňují přijímající entitě RLC provádět kritické funkce, jako je opětovné sestavování paketů ve správném pořadí, detekce duplicit a v potvrzovaném režimu (AM) identifikace chybějících paketů a spouštění jejich retransmise prostřednictvím ARQ.

Historicky, jak se buněčné systémy vyvíjely od 2G GSM (které mělo jednodušší linkové protokoly) k 3G UMTS, potřeba sofistikovanějších datových služeb mimo hlas vyžadovala robustní protokol vrstvy 2. Vrstva RLC a její formát PDU byly zavedeny v UMTS pro zpracování paketově přepínaných dat s různými požadavky na spolehlivost. Koncept byl zdokonalen a přenesen do LTE (Rel-8) a 5G NR. Návrh RLC-PDU řeší omezení spočívající v absenci standardizované jednotky pro řízení chyb přes rádiové rozhraní. Poskytuje jasné oddělení odpovědností: vrstva PDCP řeší zabezpečení a kompresi hlaviček, zatímco vrstva RLC prostřednictvím PDU řeší opravu chyb a řazení specifické pro logický kanál, nezávisle na kanálovém kódování a procesech HARQ fyzické vrstvy. Tento vrstvený přístup umožňuje efektivnější a flexibilnější správu rádiových prostředků.

## Klíčové vlastnosti

- Režimově specifické formátování (TM, UM, AM)
- Obsahuje hlavičku s pořadovým číslem (Sequence Number, SN) pro řazení
- Podporuje segmentaci a konkatenaci SDU
- Umožňuje automatický opakovaný dotaz (Automatic Repeat Request, ARQ) v AM prostřednictvím polí pro hlášení stavu
- Umožňuje doručování ve správném pořadí do horních vrstev
- Umožňuje detekci a zahození duplicit

## Související pojmy

- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [ARQ – Automatic Repeat Request](/mobilnisite/slovnik/arq/)

## Definující specifikace

- **TR 26.936** (Rel-19) — Audio Codec Characterization Technical Report

---

📖 **Anglický originál a plná specifikace:** [RLC-PDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/rlc-pdu/)
