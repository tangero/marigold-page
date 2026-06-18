---
slug: "m-hc"
url: "/mobilnisite/slovnik/m-hc/"
type: "slovnik"
title: "M-HC – Mobile Header Compressor"
date: 2025-01-01
abbr: "M-HC"
fullName: "Mobile Header Compressor"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/m-hc/"
summary: "Entita v mobilním terminálu (UE), která provádí kompresi hlaviček na vzestupných datových paketech. Snižuje režii hlaviček IP/UDP/RTP, čímž zlepšuje spektrální účinnost a snižuje latenci pro služby v"
---

M-HC je entita v mobilním terminálu, která provádí kompresi hlaviček na vzestupných paketech za účelem snížení režie IP/UDP/RTP, čímž zlepšuje spektrální účinnost a snižuje latenci pro služby v reálném čase.

## Popis

Mobile Header Compressor (M-HC) je funkční entita implementovaná ve vrstvě [PDCP](/mobilnisite/slovnik/pdcp/) (Packet Data Convergence Protocol) v uživatelském zařízení (UE) v sítích 3GPP UMTS a LTE. Jejím hlavním úkolem je aplikovat algoritmy komprese hlaviček na vzestupné IP datové pakety před jejich přenosem přes rádiové rozhraní. M-HC pracuje na úrovni jednotlivých rádiových přenosů (per-radio bearer), komprimuje často rozsáhlé a opakující se hlavičky protokolů jako IPv4, IPv6, [UDP](/mobilnisite/slovnik/udp/) a [RTP](/mobilnisite/slovnik/rtp/). Analýzou statických a dynamických polí v těchto hlavičkách nahrazuje úplnou hlavičku mnohem menším identifikátorem kontextu a komprimovanými informacemi hlavičky pro následující pakety stejného toku. Tento proces je řízen stavovými automaty definovanými ve specifikacích jako [RFC](/mobilnisite/slovnik/rfc/) 2507, RFC 3095 ([ROHC](/mobilnisite/slovnik/rohc/)) a RFC 5795, které M-HC implementuje, aby udržoval synchronizaci s odpovídajícím dekompresorem v síti (U-HD). Kompresor udržuje kompresní kontext obsahující statická pole původní hlavičky a dynamická pole z posledního přeneseného paketu. Pro každý nový paket porovná jeho hlavičku s tímto kontextem, vygeneruje komprimovaný paket obsahující pouze změny (delta) nebo identifikátor kontextu a odpovídajícím způsobem aktualizuje svůj vnitřní stav. M-HC je klíčovou součástí pro efektivní provoz služeb VoIP (Voice over IP), video streamingu a dalších interaktivních služeb přes mobilní sítě, protože přímě snižuje omezení šířky pásma a režii paketů, které jsou pro bezdrátové spoje typické.

## K čemu slouží

M-HC byl zaveden, aby řešil výraznou neefektivitu přenosu plných hlaviček IP/[UDP](/mobilnisite/slovnik/udp/)/[RTP](/mobilnisite/slovnik/rtp/) přes rádiové prostředky s omezenou šířkou pásma a vysokými náklady v sítích 3G UMTS. Rané služby založené na IP, zejména VoIP, trpěly nízkou spektrální účinností, protože datová část (např. hlasový rámec) mohla být menší než 40-60 bytů potřebných pro hlavičky. Tato režie drasticky snižovala počet současných uživatelů, které buňka mohla podporovat, a zvyšovala latenci. Vytvoření M-HC spolu s jeho protějškem na straně sítě poskytlo standardizovanou metodu pro kompresi těchto hlaviček až na 1-4 byty pro následující pakety v toku, což dramaticky zvýšilo kapacitu. Vyřešil problém s umožněním nákladově efektivního, vysoce kvalitního paketového přenosu hlasu a multimédií v reálném čase přes systémy 3GPP, což bylo zásadní pro konkurenceschopnost vůči službám s přepojováním okruhů a pro umožnění evoluce k plně IP sítím. Jeho integrace do vrstvy [PDCP](/mobilnisite/slovnik/pdcp/) zajistila těsné propojení s řízením rádiových přenosů a bezpečnostními funkcemi.

## Klíčové vlastnosti

- Nachází se ve vrstvě PDCP v UE pro zpracování vzestupného proudu
- Implementuje framework Robust Header Compression (ROHC) a jeho profily
- Udržuje kompresní kontexty pro každý rádiový přenos a tok
- Snižuje hlavičky IP/UDP/RTP z přibližně 40-60 bytů na 1-4 byty pro následující pakety
- Pracuje se stavovými automaty (např. stavy IR, FO, SO) pro robustnost
- Synchronizuje se s dekompresorem U-HD v síti pomocí zpětnovazebních kanálů

## Související pojmy

- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [ROHC – Robust Header Compression](/mobilnisite/slovnik/rohc/)

## Definující specifikace

- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification

---

📖 **Anglický originál a plná specifikace:** [M-HC na 3GPP Explorer](https://3gpp-explorer.com/glossary/m-hc/)
