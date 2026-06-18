---
slug: "vad"
url: "/mobilnisite/slovnik/vad/"
type: "slovnik"
title: "VAD – Voice Activity Detection"
date: 2025-01-01
abbr: "VAD"
fullName: "Voice Activity Detection"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vad/"
summary: "Technika zpracování signálu, která identifikuje úseky řeči a ticha v hlasovém signálu. Je klíčová pro umožnění nespojitého přenosu (DTX), který šetří baterii a rádiové zdroje tím, že přenos probíhá po"
---

VAD je technika zpracování signálu, která identifikuje úseky řeči a ticha v hlasovém signálu za účelem umožnění nespojitého přenosu (DTX), čímž šetří baterii a rádiové zdroje.

## Popis

Voice Activity Detection (VAD) je základní součástí rámce řečových kodeků 3GPP a funguje jako algoritmus digitálního zpracování signálu. Jeho primární funkcí je analyzovat vstupní zvukový signál z mikrofonu a klasifikovat každý rámec (typicky 20 ms) buď jako obsahující aktivní řeč, nebo jako neaktivní (ticho nebo šum na pozadí). Algoritmus funguje tak, že ze signálu extrahuje a analyzuje různé akustické parametry. Tyto parametry typicky zahrnují krátkodobou energii, rychlost průchodu nulou, spektrální charakteristiky a často i dlouhodobé měření spektra šumu na pozadí. Porovnáním těchto parametrů s adaptivními prahy odvozenými z odhadované úrovně šumu provádí VAD binární rozhodnutí o přítomnosti řeči.

Architektura VAD je těsně integrována s řečovým kodekem (např. [AMR](/mobilnisite/slovnik/amr/), [AMR-WB](/mobilnisite/slovnik/amr-wb/), [EVS](/mobilnisite/slovnik/evs/)). Nachází se v přenosové cestě uživatelského zařízení (UE). Když VAD klasifikuje rámec jako neaktivní, spustí činnost subsystémů nespojitého přenosu ([DTX](/mobilnisite/slovnik/dtx/)) a generování komfortního šumu ([CNG](/mobilnisite/slovnik/cng/)). Namísto neefektivního přenosu skutečného šumu na pozadí vysílač v pravidelných intervalech posílá rámce deskriptoru ticha ([SID](/mobilnisite/slovnik/sid/)). Tyto SID rámce obsahují kompaktní parametrickou reprezentaci charakteristik šumu na pozadí (např. spektrální obálku), což umožňuje systému CNG v přijímači syntetizovat podobný šum, čímž se zabrání nepřirozenému efektu „hluchého ticha“ a zachovává se přirozenost hovoru.

Klíčovými součástmi systému VAD jsou modul extrakce příznaků, algoritmus odhadu a aktualizace šumu, rozhodovací logika a mechanizma prodlevy (hangover). Mechanizmus prodlevy je zásadní; krátce prodlužuje rozhodnutí „řeč aktivní“ i po poklesu energie pod práh. Tím zabraňuje ořezávání řečových zvuků s nízkou energií, jako jsou frikativy nebo konce slov, a tím zlepšuje kvalitu řeči. Odhadovač šumu průběžně aktualizuje svůj model akustického prostředí na pozadí, což umožňuje VAD přizpůsobit se měnícím se podmínkám, například přechodu z tiché místnosti na hlučnou ulici. Jeho role je klíčová pro spektrální účinnost, protože přímo snižuje průměrnou bitovou rychlost hlasového hovoru, což síti umožňuje obsloužit více současných uživatelů. Je to základní funkce pro úsporu energie v mobilních zařízeních, která významně prodlužuje dobu hovoru.

## K čemu slouží

VAD byl vytvořen, aby řešil základní neefektivitu přenosu audio signálu s konstantní bitovou rychlostí během hlasového hovoru, kdy je mluvčí aktivní typicky pouze přibližně 40–60 % času. Přenos ticha nebo šumu na pozadí plnou rychlostí řečového kodeku spotřebovává cenné rádiové spektrum, zvyšuje interferenci a zbytečně vyčerpává baterii UE. Primární motivací bylo umožnit nespojitý přenos ([DTX](/mobilnisite/slovnik/dtx/)), což je úsporný režim, při kterém se rádiový vysílač UE vypíná během období ticha.

Historicky, před sofistikovaným digitálním VAD, měly analogové systémy primitivní hlasem ovládané spínače (VOX), které měly sklon ořezávat řeč a byly citlivé na šum na pozadí. 3GPP standardizovalo algoritmy VAD, aby zajistilo konzistentní vysoce kvalitní výkon ve všech kompatibilních zařízeních. Tím se vyřešil problém interoperability a byla zaručena minimální úroveň výkonu pro odhad šumu na pozadí a generování komfortního šumu, což je nezbytné pro dobrou uživatelskou zkušenost během DTX. Standardizací VAD umožnilo 3GPP dosáhnout masivního nárůstu kapacity sítě a výdrže baterie zařízení, což bylo klíčové pro komerční úspěch a rozšířené přijetí 2G (GSM), 3G a následujících generací mobilních sítí. Přímo řeší ekonomická a technická omezení bezdrátové komunikace.

## Klíčové vlastnosti

- Rámcová klasifikace řečové aktivity (aktivní/neaktivní)
- Adaptivní odhad šumu na pozadí a spektrální analýza
- Integrovaná prodleva (hangover period) pro zabránění ořezávání řeči
- Generování spouštěčů pro činnost nespojitého přenosu (DTX)
- Podpora parametrického generování komfortního šumu (CNG) pomocí SID rámců
- Konfigurovatelná citlivost a parametry pro vyvážení mezi kvalitou řeči a agresivitou detekce aktivity

## Související pojmy

- [DTX – Discontinuous Transmission](/mobilnisite/slovnik/dtx/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.092** (Rel-19) — AMR Comfort Noise for SCR Operation
- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS
- **TS 26.094** (Rel-19) — AMR Voice Activity Detector (VAD) Specification
- **TS 26.177** (Rel-19) — DSR Extended Advanced Front-end Test Sequences
- **TS 26.192** (Rel-19) — AMR-WB Comfort Noise Requirements
- **TS 26.193** (Rel-19) — AMR-WB Source Controlled Rate (SCR) Operation
- **TS 26.194** (Rel-19) — Voice Activity Detector for AMR-WB DTX
- **TS 26.226** (Rel-19) — Cellular Text Telephone Modem (CTM)
- **TS 26.230** (Rel-19) — CTM C Code Implementation for Text Transmission
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.267** (Rel-19) — eCall In-band Modem Specification
- **TS 26.269** (Rel-19) — eCall In-band Modem Conformance Testing
- **TS 26.441** (Rel-19) — EVS Audio Processing Introduction
- **TS 26.442** (Rel-19) — EVS Codec Fixed Point ANSI-C Code
- … a dalších 23 specifikací

---

📖 **Anglický originál a plná specifikace:** [VAD na 3GPP Explorer](https://3gpp-explorer.com/glossary/vad/)
