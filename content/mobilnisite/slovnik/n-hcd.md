---
slug: "n-hcd"
url: "/mobilnisite/slovnik/n-hcd/"
type: "slovnik"
title: "N-HCD – Network Header Compressor/Decompressor"
date: 2025-01-01
abbr: "N-HCD"
fullName: "Network Header Compressor/Decompressor"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/n-hcd/"
summary: "Souhrnný termín pro funkce komprese a dekomprese hlaviček na straně sítě, zahrnující jak N-HC (kompresor pro downlink), tak N-HD (dekompresor pro uplink). Představuje kompletní funkcionalitu ROHC ve v"
---

N-HCD je integrovaná entita na straně sítě ve vrstvě PDCP řadiče RNC, která provádí jak kompresi, tak dekompresi hlaviček za účelem optimalizace obousměrného IP provozu přes rozhraní vzdušného rozhraní.

## Popis

Network Header Compressor/Decompressor (N-HCD) není samostatnou funkční entitou, ale konceptuálním zastřešujícím termínem používaným ve specifikacích 3GPP pro označení kombinovaných schopností komprese a dekomprese hlaviček umístěných v síti, konkrétně v řadiči rádiové sítě (RNC) sítě UMTS. V praxi zahrnuje dvě odlišné operační entity: Network Header Compressor ([N-HC](/mobilnisite/slovnik/n-hc/)) a Network Header Decompressor ([N-HD](/mobilnisite/slovnik/n-hd/)). Terminologie N-HCD zdůrazňuje roli RNC jako plně duplexního ROHC protějšku k uživatelskému zařízení (UE). Ve směru downlink (síť k UE) aplikuje komponenta N-HC algoritmy robustní komprese hlaviček (ROHC) na toky IP paketů, nahrazuje rozsáhlé hlavičky stručnými identifikátory kontextu a komprimovanými daty. Ve směru uplink (UE k síti) přijímá komponenta N-HD komprimované pakety od kompresoru UE (U-HC), používá sdílený kompresní kontext k rekonstrukci původních plných hlaviček a předává kompletní pakety směrem k jádru sítě. Implementace N-HCD ve vrstvě PDCP zajišťuje těsnou integraci se správou rádiových přenosových kanálů a zpracováním QoS. Udržuje synchronizované kompresní kontexty pro každé UE a každý tok, zpracovává procedury inicializace kontextu, aktualizace, ověřování a obnovy po chybě, jak je definováno ve standardu ROHC. Stavové automaty pro kompresi a dekompresi pracují nezávisle na každém směru, ale sdílejí řídicí logiku pro optimalizaci výkonu a využití zdrojů v RNC.

## K čemu slouží

Termín N-HCD byl definován, aby poskytl holistický pohled na odpovědnost sítě v obousměrném systému komprese hlaviček požadovaném standardem 3GPP pro UMTS. Zatímco jednotlivé komponenty ([N-HC](/mobilnisite/slovnik/n-hc/) a [N-HD](/mobilnisite/slovnik/n-hd/)) mají specifické směrové role, jejich kombinovaná činnost je nezbytná pro optimalizaci veškerého provozu v uživatelské rovině. Účelem nasazení plné funkce N-HCD v RNC bylo centralizovat složitost a správu stavů protokolu ROHC v síťové infrastruktuře. Tento návrh odlehčuje výpočetní zátěž od mobilních zařízení s omezeným výkonem, protože UE potřebuje implementovat pouze komplementární polovinu (U-HC a U-HD). Zajišťuje konzistentní vynucování kompresních politik, správu kontextů a interoperabilitu mezi různými implementacemi UE. Tím, že složitější mechanismy obnovy kontextu a robustnosti zvládá strana sítě, je zlepšena celková spolehlivost systému pro služby reálného času přes nespolehlivá rádiová spojení. Koncept N-HCD zdůrazňuje, že komprese hlaviček není jednosměrnou optimalizací, ale základní síťovou funkcí pro zvýšení kapacity a kvality uživatelského zážitku u všech paketově spínaných služeb.

## Klíčové vlastnosti

- Zahrnuje jak funkci komprese (N-HC), tak dekomprese (N-HD) v rámci RNC
- Působí jako plně duplexní ROHC protistrana ke kompresoru/dekompresoru hlaviček v UE
- Spravuje obousměrné kompresní kontexty pro více UE a toků současně
- Integruje se s PDCP pro konfiguraci komprese s ohledem na QoS na úrovni přenosového kanálu
- Implementuje ROHC zpětnovazební kanály pro synchronizaci kontextu a obnovu po chybě
- Poskytuje síťově řízený ukotvovací bod pro kompresní algoritmy a parametry

## Související pojmy

- [N-HC – Network Header Compressor](/mobilnisite/slovnik/n-hc/)
- [N-HD – Network Header Decompressor](/mobilnisite/slovnik/n-hd/)

## Definující specifikace

- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification

---

📖 **Anglický originál a plná specifikace:** [N-HCD na 3GPP Explorer](https://3gpp-explorer.com/glossary/n-hcd/)
