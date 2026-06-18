---
slug: "m-hcd"
url: "/mobilnisite/slovnik/m-hcd/"
type: "slovnik"
title: "M-HCD – Mobile Header Compressor/Decompressor"
date: 2025-01-01
abbr: "M-HCD"
fullName: "Mobile Header Compressor/Decompressor"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/m-hcd/"
summary: "Kombinovaná entita v mobilním terminálu (UE), která provádí kompresi hlaviček pro uplink i dekompresi hlaviček pro downlink. Jedná se o integrovaný funkční blok ve vrstvě PDCP v UE, který zajišťuje ob"
---

M-HCD je integrovaný funkční blok ve vrstvě PDCP mobilního terminálu, který provádí kompresi hlaviček pro uplink i dekompresi hlaviček pro downlink.

## Popis

Mobile Header Compressor/Decompressor (M-HCD) představuje jednotnou funkční entitu ve vrstvě Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) uživatelského zařízení (UE), která je zodpovědná za všechny operace komprese a dekomprese hlaviček. V praxi sdružuje samostatné funkce [M-HC](/mobilnisite/slovnik/m-hc/) (kompresor) a [M-HD](/mobilnisite/slovnik/m-hd/) (dekompresor) do jediného logického bloku pro efektivitu implementace. Pro uplinkový provoz funguje M-HCD jako kompresor (M-HC) a aplikuje algoritmy jako Robust Header Compression ([ROHC](/mobilnisite/slovnik/rohc/)) na IP, [UDP](/mobilnisite/slovnik/udp/) a [RTP](/mobilnisite/slovnik/rtp/) hlavičky před odesláním paketů přes rozhraní rádiového přístupu do sítě. Spravuje kompresní kontexty, sleduje toky paketů a používá stavové stroje pro zajištění robustního provozu i v podmínkách ztrátového rádiového spojení. Pro downlinkový provoz funguje jako dekompresor (M-HD), přijímá komprimované pakety od síťového kompresoru (U-HC) a používá sdílený kontext k rekonstrukci původních plných hlaviček před předáním paketů výše v zásobníku protokolů do IP vrstvy. M-HCD řídí synchronizaci mezi svou kompresní a dekompresní stranou, zpracovává zpětnovazební zprávy (pokud je to podporováno profilem) a provádí procedury obnovy po chybě při detekci poškození kontextu nebo desynchronizace. Jeho integrace do PDCP mu umožňuje využívat bezpečnostní funkce (jako šifrování a ochrana integrity) a správu rádiových přenosových kanálů, což zajišťuje, že komprimované pakety jsou správně asociovány s příslušnými QoS toky a bezpečnostními kontexty.

## K čemu slouží

Koncept M-HCD byl standardizován, aby poskytl kompletní obousměrné řešení pro zpracování hlaviček v rámci UE, a řešil tak potřebu efektivního zpracování IP paketů v obou směrech přenosu přes rádiový spoj. Před zavedením komprese hlaviček vyžadovaly symetrické služby v reálném čase, jako je VoIP, plné hlavičky v uplinku i downlinku, což zdvojnásobovalo plýtvání přenosovou kapacitou. Integrací komprese a dekomprese do jedné entity zajistilo 3GPP koherentní implementaci, která dokáže současně spravovat stavové kontexty potřebné pro [ROHC](/mobilnisite/slovnik/rohc/) v obou směrech. Tím se vyřešil problém nekonzistentní implementace a potenciálních problémů s interoperabilitou mezi samostatnými moduly kompresoru a dekompresoru. Zjednodušilo to také návrh a testování UE, protože M-HCD mohl být považován za jednotnou funkci protokolu v rámci [PDCP](/mobilnisite/slovnik/pdcp/). Vytvoření M-HCD bylo motivováno vizí 3GPP sítí jako plně IP, kde maximalizace spektrální účinnosti pro paketově přepínaný hlas, video a data byla klíčová pro komerční životaschopnost a uživatelský zážitek.

## Klíčové vlastnosti

- Integrovaná entita kombinující funkce M-HC a M-HD ve vrstvě PDCP v UE
- Provádí kompresi hlaviček pro uplink pomocí ROHC a dalších algoritmů
- Provádí dekompresi hlaviček pro downlink k rekonstrukci původních paketů
- Spravuje obousměrné kompresní kontexty a synchronizaci stavů
- Zpracovává zpětnovazební kanály ROHC pro robustnost a obnovu po chybě
- Těsně integrováno s bezpečnostními funkcemi PDCP (šifrování/integrální ochrana) a mapováním přenosových kanálů

## Související pojmy

- [M-HC – Mobile Header Compressor](/mobilnisite/slovnik/m-hc/)
- [M-HD – Mobile Header Decompressor](/mobilnisite/slovnik/m-hd/)
- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [ROHC – Robust Header Compression](/mobilnisite/slovnik/rohc/)

## Definující specifikace

- **TS 25.323** (Rel-19) — Packet Data Convergence Protocol (PDCP) Specification

---

📖 **Anglický originál a plná specifikace:** [M-HCD na 3GPP Explorer](https://3gpp-explorer.com/glossary/m-hcd/)
