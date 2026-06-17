---
slug: "n-hc"
url: "/mobilnisite/slovnik/n-hc/"
type: "slovnik"
title: "N-HC – Network Header Compressor"
date: 2025-01-01
abbr: "N-HC"
fullName: "Network Header Compressor"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/n-hc/"
summary: "Entita v síti, typicky v PDCP vrstvě RNC, která provádí kompresi hlaviček na downlinkových datových paketech. Snižuje režii hlaviček IP/UDP/RTP k úspoře rádiové šířky pásma a zlepšení spektrální účinn"
---

N-HC je síťová entita, typicky v PDCP vrstvě RNC, která komprimuje hlavičky IP/UDP/RTP na downlinkových paketech za účelem úspory rádiové šířky pásma a zlepšení spektrální účinnosti.

## Popis

Network Header Compressor (N-HC) je funkční entita definovaná v architektuře 3GPP UMTS Radio Access Network (UTRAN), která se konkrétně nachází v Radio Network Controller (RNC). Její primární implementace je v rámci Packet Data Convergence Protocol (PDCP) vrstvy. N-HC funguje na downlinkové cestě, což znamená, že zpracovává datové pakety směřující ze základnové sítě k User Equipment (UE). Její hlavní funkcí je aplikace robustních algoritmů komprese hlaviček (ROHC) na IP provoz, jako je VoIP (používající RTP/UDP/IP) nebo interaktivní webový provoz (TCP/IP). Kompresor analyzuje hlavičky paketů, identifikuje statická a dynamická pole a nahrazuje plné hlavičky v následujících paketech mnohem kratšími identifikátory kontextu a komprimovanými informacemi hlaviček. Tento proces vytváří a udržuje kompresní kontext jak na straně N-HC, tak u jejího partnerského entity, dekompresoru hlaviček v UE (U-HD). Kontext obsahuje statické informace a měnící se vzory polí hlaviček, což umožňuje dekompresoru rekonstruovat původní hlavičky. N-HC je zodpovědná za inicializaci, aktualizaci a správu kontextu, zajišťuje synchronizaci s dekompresorem i při ztrátě paketů. Díky drastickému zmenšení velikosti hlaviček z 40-60 bajtů pro IPv4/v6 na několik bajtů N-HC přímo zvyšuje kapacitu užitečných dat každého rádiového transportního bloku, což vede k efektivnějšímu využití vzácného a drahého rádiového spektra. Její činnost je transparentní pro vyšší vrstvy a je konfigurovatelná na rádiový bearer podle profilu QoS, což umožňuje síťovým operátorům selektivně aplikovat kompresi pro maximalizaci zisku u aplikací citlivých na zpoždění a s nízkou šířkou pásma.

## K čemu slouží

N-HC byla zavedena k řešení významné neefektivity přenosu plných IP hlaviček přes šířkou pásma omezené a na chyby náchylné buněčné rádiové rozhraní. V raných paketových mobilních datových službách mohla režie z IP, UDP a RTP hlaviček tvořit 60-80 % paketu u služeb s malým užitečným zatížením, jako je Voice over IP (VoIP), což takové služby činilo ekonomicky a technicky neproveditelnými. Primární motivací bylo umožnit efektivní podporu služeb reálného času s nízkou přenosovou rychlostí přes sítě UMTS, což byl klíčový cíl 3GPP Release 5. Bez komprese hlaviček by byla spektrální účinnost pro konverzační služby nepřijatelně nízká, plýtvalo by se kapacitou a zvyšovalo se zpoždění. N-HC jako součást ROHC frameworku standardizovaného v [IETF](/mobilnisite/slovnik/ietf/) a přijatého 3GPP toto vyřešila přesunutím složité kompresní logiky na stabilní síťovou stranu (RNC), což umožnilo jednodušší dekompresi v UE. Tato architektonická volba vyvážila složitost zpracování a spotřebu energie, zajistila, že životnost baterie UE nebyla nadměrně ovlivněna, a zároveň dosáhla nezbytných úspor šířky pásma k umožnění služeb jako videotelefonie a VoIP přes 3G sítě.

## Klíčové vlastnosti

- Umístěna v PDCP vrstvě RNC pro kompresi downlinkového provozu
- Implementuje profily Robust Header Compression (ROHC) (např. pro IP, UDP, RTP, ESP)
- Vytváří a spravuje kompresní kontexty synchronizované s dekompresorem v UE
- Dynamicky přizpůsobuje stav komprese (např. Inicializace, Prvního řádu, Druhého řádu) na základě spolehlivosti spoje
- Konfigurovatelná na rádiový bearer podle požadavků QoS a typu provozu
- Poskytuje robustnost vůči ztrátě paketů a zbytkovým chybám na rádiovém spoji

## Definující specifikace

- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification

---

📖 **Anglický originál a plná specifikace:** [N-HC na 3GPP Explorer](https://3gpp-explorer.com/glossary/n-hc/)
