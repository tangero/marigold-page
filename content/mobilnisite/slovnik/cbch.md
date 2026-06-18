---
slug: "cbch"
url: "/mobilnisite/slovnik/cbch/"
type: "slovnik"
title: "CBCH – Cell Broadcast Channel"
date: 2025-01-01
abbr: "CBCH"
fullName: "Cell Broadcast Channel"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cbch/"
summary: "CBCH je jednosměrný kanál typu point-to-multipoint v sítích GSM/UMTS pro vysílání krátkých zpráv na všechna mobilní zařízení v určité geografické oblasti, známé jako buňka. Umožňuje hromadné výstražné"
---

CBCH je jednosměrný vysílací kanál v sítích GSM/UMTS sloužící k odesílání krátkých zpráv, jako jsou veřejná varování nebo dopravní upozornění, na všechna mobilní zařízení v konkrétní buňce, aniž by způsoboval zahlcení sítě.

## Popis

Kanál pro buňkové vysílání (Cell Broadcast Channel – CBCH) je základním vysílacím mechanismem v architektuře rádiového přístupového sítě GSM a UMTS, navrženým pro efektivní jednosměrnou distribuci informací. Funguje jako logický kanál mapovaný na fyzické zdroje, konkrétně využívá vyhrazený časový slot na nosné kanálu řídicího vysílání ([BCCH](/mobilnisite/slovnik/bcch/)) v GSM nebo příslušné transportní kanály v UMTS. Systém je řízen Centrem pro buňkové vysílání ([CBC](/mobilnisite/slovnik/cbc/)), entitou jádra sítě, která vytváří vysílací zprávy a předává je prostřednictvím řídicí stanice základny ([BSC](/mobilnisite/slovnik/bsc/)) v GSM nebo řídicí stanice rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS k přenosové stanici ([BTS](/mobilnisite/slovnik/bts/)) nebo Node B pro vysílání přes rozhraní prostorového přenosu. Každá vysílaná zpráva je označena identifikátorem zprávy a sériovým číslem, což mobilním stanicím umožňuje filtrovat a zobrazovat relevantní informace na základě uživatelských preferencí nebo síťových požadavků.

Z technického hlediska jsou zprávy CBCH formátovány jako krátké řetězce o délce až 93 znaků (v GSM) a jsou opakovaně vysílány v definované geografické oblasti, známé jako buňka nebo skupina buněk tvořících oblast umístění ([LA](/mobilnisite/slovnik/la/)) nebo oblast směrování ([RA](/mobilnisite/slovnik/ra/)). Vysílání probíhá na specifickém logickém kanálu CBCH, který je multiplexován s dalšími řídicími kanály. Mobilní zařízení tento kanál nepřetržitě monitorují, když jsou připojena k buňce, a dekódují zprávy bez navázání vyhrazeného spojení, čímž pracují v režimu nečinnosti. Tento návrh zajišťuje minimální dopad na kapacitu sítě a výdrž baterie zařízení, protože není vyžadován žádný přenos v uplinku ani potvrzení.

Architektura zahrnuje klíčová rozhraní: CBC se připojuje k BSC přes rozhraní [CBC-BSC](/mobilnisite/slovnik/cbc-bsc/) (standardizované v 3GPP TS 48.049) za použití Protokolu pro buňkové vysílání (CBP). V rádiové přístupové síti BSC mapuje data CBCH na pomalu přidružený řídicí kanál (SACCH) pro přenos s využitím předdefinované struktury časových slotů. Plánování zpráv a míra opakování jsou konfigurovatelné, což umožňuje síťovým operátorům upřednostnit kritická upozornění. Bezpečnostní aspekty zahrnují integritu zpráv prostřednictvím sériového číslování, ale tradiční CBCH postrádá šifrování, což jej činí vhodným pro veřejné informace, nikoli pro důvěrná data. Jeho role přesahuje pouhé zasílání zpráv; podporuje Službu buňkového vysílání (CBS), která umožňuje aplikace jako systém varování před zemětřesením a tsunami (ETWS) nebo komerční mobilní výstražný systém (CMAS), které jsou klíčové pro veřejnou bezpečnost.

## K čemu slouží

CBCH byl vytvořen k uspokojení potřeby efektivního šíření informací v široké oblasti mobilních sítí bez způsobení zahlcení spojeného s bodovou službou krátkých zpráv (SMS). Před jeho zavedením vyžadovalo vysílání informací individuální doručení SMS každému účastníkovi, což při mimořádných událostech nebo událostech s vysokou poptávkou přetěžovalo síťové zdroje. CBCH tento problém řeší využitím paradigmatu jeden-všem (one-to-many), což zajišťuje, že jediný přenos zprávy dosáhne současně všech zařízení v cílové buňce bez ohledu na počet uživatelů. Tato schopnost je zásadní pro časově citlivá upozornění, jako jsou varování před přírodními katastrofami, kde je rychlá a spolehlivá komunikace nezbytná pro veřejnou bezpečnost.

Historicky byl CBCH standardizován v 3GPP Release 4 jako součást vylepšení GSM Phase 2+, vyvinut z dřívějších specifikací GSM pro podporu služeb s přidanou hodnotou. Jeho vývoj byl motivován rostoucí poptávkou po službách založených na poloze a regulatorními požadavky na systémy veřejného varování v různých zemích. Odlehčením vysílacího provozu od vyhrazených signalizačních kanálů CBCH zlepšuje efektivitu a škálovatelnost sítě a umožňuje operátorům nabízet komerční služby, jako je reklama nebo aktualizace zpráv, bez zhoršení výkonu hlasových nebo datových služeb. Tato technologie položila základy pro pozdější pokroky v systému upozornění na varování v LTE a systému veřejného varování v 5G, při zachování zpětné kompatibility napříč generacemi.

## Klíčové vlastnosti

- Jednosměrné vysílání typu point-to-multipoint
- Geografické cílení na úrovni buňky nebo oblasti umístění
- Nevyžaduje vyhrazené spojení (mobil v režimu nečinnosti)
- Podpora identifikátorů zpráv a sériového číslování pro filtrování
- Konfigurovatelné míry opakování a plánování
- Integrace s Centrem pro buňkové vysílání (CBC) pro správu sítě

## Související pojmy

- [CBS – Cell Broadcast Service](/mobilnisite/slovnik/cbs/)
- [SDCCH – Stand-Alone Dedicated Control Channel](/mobilnisite/slovnik/sdcch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TS 48.049** (Rel-19) — Cell Broadcast Service Protocol Specification
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [CBCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbch/)
