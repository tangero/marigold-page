---
slug: "rclwi"
url: "/mobilnisite/slovnik/rclwi/"
type: "slovnik"
title: "RCLWI – RAN Controlled LTE-WLAN Interworking"
date: 2025-01-01
abbr: "RCLWI"
fullName: "RAN Controlled LTE-WLAN Interworking"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rclwi/"
summary: "Síťová architektura, ve které uzel rádiového přístupového sítě (RAN) (eNB) řídí směrování uživatelského provozu mezi rádiovými rozhraními LTE a WLAN. Umožňuje těsnější integraci a inteligentnější dist"
---

RCLWI je síťová architektura 3GPP, ve které uzel RAN řídí směrování provozu mezi LTE a WLAN za účelem těsnější integrace a inteligentnější distribuce založené na aktuálních rádiových podmínkách.

## Popis

RAN Controlled LTE-WLAN Interworking (RCLWI) je funkce 3GPP zavedená ve vydání Release 13, která umožňuje LTE eNodeB ([eNB](/mobilnisite/slovnik/enb/)) rozhodovat a provádět směrování provozu mezi LTE a důvěryhodnou [WLAN](/mobilnisite/slovnik/wlan/) přístupovou sítí pro koncové zařízení (UE). V této architektuře eNB využívá měřící hlášení od UE o rádiových podmínkách LTE i WLAN (např. LTE [RSRP](/mobilnisite/slovnik/rsrp/)/[RSRQ](/mobilnisite/slovnik/rsrq/) a WLAN [RSSI](/mobilnisite/slovnik/rssi/), vytížení kanálu, propustnost backhaulového spoje) k rozhodnutí, zda přenést datový provoz na WLAN, nebo jej ponechat na LTE. eNB poté poskytne příkazy pro směrování UE prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/), kterými mu nařídí směrovat provoz pro konkrétní Access Point Names ([APN](/mobilnisite/slovnik/apn/)) nebo přenosové kanály přes WLAN.

Procedura zahrnuje několik klíčových komponent. UE musí podporovat jak LTE, tak WLAN rádiové rozhraní a potřebná rozšíření pro měřící hlášení definovaná v 36.331. eNB je rozšířeno o logiku RCLWI a komunikuje s důvěryhodnou WLAN přístupovou sítí ([TWAN](/mobilnisite/slovnik/twan/)) přes rozhraní Xw (specifikované v 36.463). Entity jádra sítě, konkrétně MME a PGW, jsou zapojeny do správy relací, ale nejsou místem rozhodování o směrování. Když se eNB rozhodne provoz přesměrovat, může nařídit UE, aby navázalo spojení s konkrétní WLAN a směrovalo vybrané IP toky. UE využívá pro připojení svého provozu k PGW přes TWAN tunely IPsec (přes IKEv2) nebo podobné mechanismy, čímž zajišťuje plynulou mobilitu a kontinuitu relace pro přesměrované přenosové kanály.

RCLWI umožňuje podrobnější a dynamičtější správu provozu ve srovnání s dřívějšími řešeními řízenými jádrem sítě, jako je ANDSF nebo non-seamless WLAN offload. Protože eNB má aktuální informace o rádiovém prostředí na úrovni buňky, může činit rychlejší a kontextově povědomější rozhodnutí o směrování, čímž optimalizuje celkové využití rádiových prostředků a uživatelský zážitek. Podporuje směrování provozu v uplinku i downlinku a může být použito pro vyrovnávání zatížení nebo využití WLAN pro zvýšení kapacity. Architektura zachovává kontrolu jádra sítě nad autentizací a politikami, přičemž deleguje výběr přístupu na RAN.

## K čemu slouží

RCLWI bylo vytvořeno za účelem řešení omezení dřívějších řešení pro propojení LTE a WLAN, která byla primárně řízena jádrem sítě (např. pomocí politik ANDSF) nebo samotným UE. Tyto přístupy často postrádaly aktuální povědomí o lokálním rádiovém prostředí, což vedlo k neoptimálním rozhodnutím o směrování, jako je přesměrování provozu na přetíženou WLAN nebo setrvání na slabé LTE buňce. Potřeba těsnější a inteligentnější integrace rostla s tím, jak se WLAN stala všudypřítomnou a operátoři ji chtěli využívat jako komplementární technologii rádiového přístupu.

Primární problém, který RCLWI řeší, je neefektivní využití kombinovaných zdrojů LTE a WLAN. Umístěním kontroly do RAN umožňuje, aby se rozhodnutí o směrování zakládala na okamžitých rádiových podmínkách, zatížení sítě a politikách operátora na hranici buňky. To vede k lepšímu vyrovnávání zatížení, zvýšení celkové kapacity sítě a lepší propustnosti pro uživatele. Poskytuje operátorům přímou kontrolu nad distribucí provozu v jejich rádiové stopě.

Historicky bylo RCLWI součástí širšího úsilí 3GPP ve vydání Release 13 a následujících (v rámci LTE-WLAN Aggregation/LWA) o hlubokou integraci WLAN do architektury mobilní sítě. Reagovalo na explozivní nárůst datového provozu a potřebu plynule využívat všechny dostupné přístupové technologie. RCLWI nabídlo citlivější alternativu ke statickým politikám ANDSF, umožňující dynamické směrování provozu, které se dokáže přizpůsobit měnícím se podmínkám, což v konečném důsledku zlepšuje efektivitu sítě a uživatelský zážitek v heterogenních sítích.

## Klíčové vlastnosti

- eNB činí rozhodnutí o směrování v reálném čase na základě měření UE parametrů LTE a WLAN
- Používá signalizaci RRC k předání příkazu UE pro směrování provozu na/z WLAN
- Podporuje směrování konkrétních IP toků nebo APN (s granularitou na úrovni přenosového kanálu)
- Definuje rozhraní Xw mezi eNB a důvěryhodnou WLAN přístupovou sítí (TWAN)
- Umožňuje směrování provozu v uplinku i downlinku
- Zachovává relace a zabezpečení jádra sítě (např. prostřednictvím IPsec tunelů k PGW)

## Související pojmy

- [LWA – LTE-WLAN Radio Level Aggregation](/mobilnisite/slovnik/lwa/)
- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)

## Definující specifikace

- **TS 23.161** (Rel-19) — Network-based IP Flow Mobility (NBIFOM)
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.463** (Rel-19) — XwAP Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [RCLWI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rclwi/)
