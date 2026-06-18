---
slug: "sp-midi"
url: "/mobilnisite/slovnik/sp-midi/"
type: "slovnik"
title: "SP-MIDI – Scalable Polyphony MIDI"
date: 2025-01-01
abbr: "SP-MIDI"
fullName: "Scalable Polyphony MIDI"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sp-midi/"
summary: "Verze protokolu MIDI (Musical Instrument Digital Interface) přizpůsobená 3GPP pro mobilní sítě. Umožňuje efektivní přenos polyfonních hudebních dat, díky čemuž mohou vyzváněcí tóny a audio služby škál"
---

SP-MIDI je verze protokolu MIDI přizpůsobená 3GPP pro mobilní sítě, která umožňuje efektivní, škálovatelný přenos polyfonních hudebních dat, jako jsou vyzváněcí tóny, na základě možností zařízení a stavu sítě.

## Popis

Scalable Polyphony [MIDI](/mobilnisite/slovnik/midi/) (SP-MIDI) je mobilní sítím optimalizovaná audio služba standardizovaná 3GPP, podrobně popsaná ve specifikacích jako 26.140 (kodek), 26.141 (shoda) a 26.234 (přenosy). Vychází z průmyslového standardu MIDI, ale obsahuje klíčové úpravy pro omezené a proměnlivé prostředí bezdrátové komunikace. SP-MIDI definuje strukturovanou metodu pro kódování hudebních výkonů jako sekvenci událostí (zahájení tónu, ukončení tónu, změna programu, řídicí změny), která je ve srovnání se vzorkovaným audiem velmi kompaktní. Základní inovací je funkce „škálovatelnosti“, kdy jediná hudební skladba obsahuje více instrumentálních stop nebo kanálů s přiřazenou prioritou.

Architektura služby SP-MIDI zahrnuje tvůrce obsahu, síťový server a přijímající UE. Obsah je vytvářen s použitím zvukové sady General MIDI (GM) nebo Mobile [DLS](/mobilnisite/slovnik/dls/) (Downloadable Sounds) Level 2 jako základu. Škálovatelnost je implementována prostřednictvím „Channel Priority Table“ (tabulky priorit kanálů) vložené do souboru MIDI. Tato tabulka přiřadí každému z 16 kanálů MIDi úroveň priority (např. 0–15). Přijímací zařízení, které může mít omezenou polyfonii (počet současně syntetizovaných tónů, např. 4, 16 nebo 24 hlasů), tuto tabulku používá k dynamické úpravě přehrávání. Pokud je polyfonní kapacita zařízení nižší než počet aktivních tónů ve skladbě, nejprve ztlumí nebo zakáže tóny na kanálech s nejnižší prioritou, čímž zajistí, že nejdůležitější melodické a rytmické prvky jsou vždy slyšet.

Jak to funguje v praxi: Když je soubor SP-MIDI doručen na UE (např. jako stažení vyzváněcího tónu přes [MMS](/mobilnisite/slovnik/mms/) nebo streamování), mediální přehrávač zařízení analyzuje hlavičku souboru, přečte Channel Priority Table a identifikuje vlastní hardwarový limit polyfonie. Během přehrávání syntetizér sleduje počet současně aktivních tónů. Jak se tento počet blíží limitu zařízení, plánovač začne vynechávat tóny naplánované ke znění na kanálech s nejnižšími čísly priority. K tomu dochází v reálném čase, což poskytuje pozvolné snížení audio bohatství namísto úplného selhání nebo zkreslení. Protokol také podporuje stahovatelné zvukové banky (DLS) pro zajištění konzistentního zabarvení na různých zařízeních, ačkoli primární zaměření je na strukturální škálovatelnost polyfonie.

## K čemu slouží

SP-MIDI byl vytvořen v 3GPP Release 8, aby vyřešil problém doručování kvalitních polyfonních vyzváněcích tónů a audio služeb v silně fragmentovaném ekosystému mobilních telefonů s velmi odlišnými audio možnostmi. Před SP-MIDI vedly monofonní vyzváněcí tóny nebo proprietární formáty k nekonzistentní uživatelské zkušenosti a polyfonní soubory [MIDI](/mobilnisite/slovnik/midi/) mohly na zařízeních s nedostatečným počtem syntetizátorových hlasů znít poškozeně nebo být tiché. Mobilní průmysl potřeboval standardizovaný, dopředně kompatibilní formát, který by tvůrcům obsahu umožnil vytvořit jedinou hudební skladbu, která by byla přijatelně slyšitelná jak na základním telefonu se 4 hlasy, tak na prémiovém smartphonu s 64 hlasy.

Motivace pramenila z bouřlivě rostoucího trhu personalizovaných vyzváněcích tónů v letech 2000. Síťoví operátoři a poskytovatelé obsahu požadovali spolehlivou službu, kde by zakoupený vyzváněcí tón spolehlivě fungoval na jakémkoli účastnickém telefonu. SP-MIDI řešil omezení statického MIDI zavedením inteligence na straně přehrávacího zařízení. Namísto toho, aby síť musela znát možnosti každého zařízení a podle toho překódovat obsah, byla inteligence přesunuta na okraj – soubor sám nesl pravidla pro stanovení priorit a zařízení provedlo adaptaci. Tím se snížila složitost síťového zpracování a potřeba úložiště pro více verzí obsahu, a zároveň byla zaručena základní přijatelná zkušenost s přehráváním, čímž byly chráněny příjmové toky z obsahových služeb.

## Klíčové vlastnosti

- Dynamická adaptace polyfonie na základě možností zařízení
- Vestavěná Channel Priority Table (0–15) pro pozvolnou degradaci
- Založeno na zvukových sadách General MIDI a Mobile DLS Level 2
- Extrémně nízká spotřeba přenosové kapacity ve srovnání se vzorkovaným audiem
- Podpora stahovatelných zvukových bank pro konzistenci zabarvení
- Standardizovaný přenos přes 3GPP packet-switched streaming (PSS) a MMS

## Související pojmy

- [MIDI – Musical Instrument Digital Interface](/mobilnisite/slovnik/midi/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification

---

📖 **Anglický originál a plná specifikace:** [SP-MIDI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sp-midi/)
