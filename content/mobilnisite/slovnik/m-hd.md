---
slug: "m-hd"
url: "/mobilnisite/slovnik/m-hd/"
type: "slovnik"
title: "M-HD – Mobile Header Decompressor"
date: 2025-01-01
abbr: "M-HD"
fullName: "Mobile Header Decompressor"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/m-hd/"
summary: "Entita v mobilním terminálu (UE), která provádí dekompresi hlaviček na datových paketech ve směru downlink přijatých ze sítě. Rekonstruuje plné IP/UDP/RTP hlavičky z komprimovaných formátů, což umožňu"
---

M-HD je entita v mobilním terminálu, která provádí dekompresi hlaviček na datových paketech ve směru downlink, rekonstruuje plné IP/UDP/RTP hlavičky z komprimovaných formátů, čímž umožňuje efektivní využití rádiové šířky pásma.

## Popis

Mobile Header Decompressor (M-HD) je funkční entita ve vrstvě Packet Data Convergence Protocol (PDCP) v uživatelském zařízení (UE) v systémech 3GPP. Jejím specifickým úkolem je zpracovávat downlinkové pakety přijaté přes rádiové rozhraní od kompresoru hlaviček na straně sítě (U-HC). Tyto pakety přicházejí s komprimovanými hlavičkami, často redukovanými na několik bajtů obsahujících pouze rozdílové změny nebo identifikátory kontextu. M-HD využívá lokálně udržovaný dekompresní kontext, který musí být synchronizován s kontextem kompresoru, k rekonstrukci původních plných hlaviček protokolů IP, UDP, RTP a případně dalších. Dekompresní kontext obsahuje statická pole a poslední známé hodnoty dynamických polí pro daný tok paketů. Po přijetí komprimovaného paketu M-HD interpretuje formát hlavičky, aplikuje rozdílové aktualizace nebo odkazuje na kontext a znovu sestaví úplnou hlavičku tak, jak existovala před kompresí. Tento proces se řídí stejnými stavovými automaty ROHC (např. Inicializace a obnova, prvního řádu, druhého řádu) jako kompresor, což zajišťuje robustnost. M-HD může také generovat zpětnovazební pakety (potvrzení, negativní potvrzení nebo aktualizace statického kontextu) k odeslání zpět U-HC pro vyžádání retransmisí nebo signalizaci poškození kontextu, v závislosti na použitém profilu a režimu ROHC. Po úspěšné dekompresi je paket s plnou hlavičkou předán výše do IP vrstvy v UE pro další zpracování. M-HD je nezbytný pro zachování koncové transparentnosti IP služeb při využití úspor šířky pásma díky kompresi hlaviček na downlinku.

## K čemu slouží

M-HD byl vytvořen jako doplněk ke kompresoru pro uplink ([M-HC](/mobilnisite/slovnik/m-hc/)), aby umožnil plnou obousměrnou efektivitu komprese hlaviček přes rádiový spoj. V raných paketových datových službách 3G tvořil downlinkový provoz (např. prohlížení webu, streamování videa) často většinu využití šířky pásma. Přenos plných hlaviček pro každý downlinkový paket byl významným plýtváním vzácnými rádiovými prostředky. M-HD to vyřešil tím, že umožnil síti (RNC v UMTS, [eNB](/mobilnisite/slovnik/enb/) v LTE) komprimovat downlinkové hlavičky, zatímco je UE efektivně dekomprimovalo. To bylo klíčové pro ekonomickou proveditelnost služeb s vysokou šířkou pásma, jako je streamování videa a stahování velkých souborů, přes mobilní sítě. Řešilo to asymetrii raného využití mobilního internetu, kde byla kapacita downlinku klíčovým úzkým místem. Standardizací dekompresní funkce ve vrstvě PDCP v UE zajistila 3GPP interoperabilitu a konzistentní výkon, což umožnilo síťovým operátorům nasazovat kompresi hlaviček transparentně, zlepšovat uživatelské datové rychlosti a kapacitu sítě bez nutnosti změn v koncových uživatelských aplikacích.

## Klíčové vlastnosti

- Nachází se ve vrstvě PDCP v UE pro zpracování downlinku
- Rekonstruuje plné IP/UDP/RTP hlavičky z formátů komprimovaných ROHC
- Udržuje dekompresní kontexty synchronizované s kompresorem U-HC
- Implementuje stavové automaty ROHC pro robustní provoz přes ztrátové spoje
- Generuje a zpracovává zpětnovazební pakety pro opravu a synchronizaci kontextu
- Zajišťuje pořadí a integritu paketů po dekompresi před předáním do IP vrstvy

## Definující specifikace

- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification

---

📖 **Anglický originál a plná specifikace:** [M-HD na 3GPP Explorer](https://3gpp-explorer.com/glossary/m-hd/)
