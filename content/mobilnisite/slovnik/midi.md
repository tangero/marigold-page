---
slug: "midi"
url: "/mobilnisite/slovnik/midi/"
type: "slovnik"
title: "MIDI – Musical Instrument Digital Interface"
date: 2025-01-01
abbr: "MIDI"
fullName: "Musical Instrument Digital Interface"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/midi/"
summary: "Standardizovaný protokol pro přenos hudebních vystoupení a řídicích dat (note on/off, výška tónu, tempo) přes digitální sítě. V 3GPP je adaptován pro streamování interaktivního hudebního obsahu s nízk"
---

MIDI je standardizovaný protokol, který 3GPP adaptoval pro streamování interaktivních hudebních vystoupení a řídicích dat s nízkou potřebou přenosové kapacity do mobilních zařízení.

## Popis

V rámci 3GPP se termín Musical Instrument Digital Interface (MIDI) vztahuje k adaptaci a přenosu průmyslově standardního protokolu MIDI přes mobilní sítě pro multimediální služby. Na rozdíl od zvukových kodeků, které kódují zvukové vlny, MIDI přenáší instrukce – řadu zpráv popisujících hudební vystoupení, jako je 'note on' (jaký tón, na jakém kanálu, s jakou dynamikou), 'note off', změnu výšky tónu (pitch bend), řídicí změny (modulace, hlasitost) a změnu programu (výběr zvuku nástroje). Tyto zprávy jsou na přijímací straně interpretovány syntezátorem nebo zvukovým engine, který generuje zvuk. 3GPP standardizovalo specifické profily a kodeky pro MIDI obsah, aby zajistilo interoperabilitu napříč zařízeními a sítěmi. Klíčové specifikace jako 3GPP TS 26.114 definují typ média MIDI pro použití v paketové streamovací službě ([PSS](/mobilnisite/slovnik/pss/)) a službě multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)). Přenos zahrnuje zapouzdření proudu MIDI příkazů do strukturovaného zvukového formátu, často s využitím standardů General MIDI (GM) nebo Scalable Polyphony MIDI ([SP-MIDI](/mobilnisite/slovnik/sp-midi/)), aby bylo zajištěno konzistentní přehrávání na zařízeních s různými schopnostmi. SP-MIDI například umožňuje tvůrcům obsahu specifikovat, jak se má složitá MIDI sekvence adaptovat (např. které tóny vynechat), když je přehrávána na zařízení s omezenou polyfonií (méně současně znějících tónů). Pro streamování jsou MIDI data zabalena do formátu [RTP](/mobilnisite/slovnik/rtp/) přenosové jednotky (definovaného v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) a odkazovaného 3GPP) a odeslána přes síť. Mediální přehrávač v přijímacím klientovi obsahuje MIDI renderer (softwarový syntezátor), který tyto pakety interpretuje a v reálném čase generuje odpovídající zvuk. Tato architektura umožňuje vysoce efektivní přenos hudebního obsahu, neboť několikaminutová skladba pro více nástrojů může být reprezentována několika kilobajty MIDI dat, ve srovnání s megabajty pro ekvivalentní [PCM](/mobilnisite/slovnik/pcm/) audio.

## K čemu slouží

3GPP standardizovalo přenos MIDI, aby umožnilo bohaté interaktivní zvukové služby na raných mobilních sítích 2.5G a 3G, kde byla přenosová kapacita výrazně omezená a drahá. Odesílání vysoce kvalitních polyfonních vyzvánění, herních soundtracků nebo interaktivních hudebních aplikací jako komprimované [PCM](/mobilnisite/slovnik/pcm/) nebo MP3 audio bylo často nepraktické. MIDI poskytlo dokonalé řešení: nabízelo vysokou hudební věrnost (závislou na kvalitě syntezátoru zařízení) s extrémně nízkou datovou propustností, což jej činilo ideálním pro stahovatelná vyzvánění, hudební zprávy a streamování hudby na pozadí pro hry. Řešilo potřebu škálovatelného, na zařízení adaptivního zvukového formátu. Vytvoření profilů jako SP-MIDI konkrétně vyřešilo problém fragmentace zařízení – jeden MIDI soubor mohl znít přijatelně jak na špičkovém telefonu se 64hlasým syntezátorem, tak na základním modelu s pouze 4hlasou polyfonií. To pohánělo komerční úspěch polyfonních vyzvánění. Dále, událostmi řízená povaha MIDI umožnila interaktivní ovládání, což umožnilo aplikace jako výuka hudby v reálném čase nebo ovládání vzdáleného nástroje, což by s předrenderovaným zvukem nebylo možné. Jeho zařazení do standardů 3GPP bylo motivováno snahou vytvořit životaschopný ekosystém mobilní hudby předtím, než se staly široce dostupné vysokorychlostní data a efektivní percepční zvukové kodeky.

## Klíčové vlastnosti

- Přenáší příkazy pro hudební vystoupení, nikoli zvukové vlny, pro extrémní efektivitu přenosové kapacity
- Podporuje standardní MIDI zprávy (note on/off, control change, program change)
- Využívá profily jako General MIDI (GM) a Scalable Polyphony MIDI (SP-MIDI) pro konzistentní přehrávání
- Definované formáty RTP přenosových jednotek pro streamování v reálném čase přes IP sítě
- Umožňuje interaktivní a adaptivní hudební aplikace
- Používá se pro služby jako stahovatelná polyfonní vyzvánění, hudební zprávy a zvuk ve hrách

## Související pojmy

- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [SP-MIDI – Scalable Polyphony MIDI](/mobilnisite/slovnik/sp-midi/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)

## Definující specifikace

- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification

---

📖 **Anglický originál a plná specifikace:** [MIDI na 3GPP Explorer](https://3gpp-explorer.com/glossary/midi/)
