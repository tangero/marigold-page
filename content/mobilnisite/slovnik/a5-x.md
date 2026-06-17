---
slug: "a5-x"
url: "/mobilnisite/slovnik/a5-x/"
type: "slovnik"
title: "A5/X – Encryption Algorithm A5/0-7"
date: 2025-01-01
abbr: "A5/X"
fullName: "Encryption Algorithm A5/0-7"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/a5-x/"
summary: "Rodina proudových šifrovacích algoritmů používaných pro šifrování uživatelských dat a signalizace přes rozhraní vzdušného rozhraní v sítích GSM a raných sítích UMTS. Chrání důvěrnost komunikace mezi m"
---

A5/X je rodina proudových šifrovacích algoritmů používaných pro šifrování dat a signalizace přes rozhraní vzdušného rozhraní v sítích GSM a raných sítích UMTS, přičemž její varianty (A5/0 až A5/7) nabízejí různou úroveň zabezpečení.

## Popis

Algoritmy A5/X jsou soubor proudových šifer standardizovaných 3GPP pro zabezpečení rádiového spoje v GSM (2G) a v některých raných implementacích pro okruhově spínaná spojení v UMTS (3G). Fungují v rámci mobilní stanice (MS) a základnové přijímací stanice (BTS) za účelem šifrování bitového proudu mezi těmito koncovými body. Základní mechanismus spočívá v generování pseudonáhodného šifrovacího klíčového proudu na základě tajného sezení klíče (Kc) odvozeného během autentizace, který je následně kombinován (obvykle pomocí XOR) s otevřeným textem za vzniku šifrovaného textu. Konkrétní varianta (např. A5/1, A5/2, A5/3) určuje vnitřní logiku algoritmu, přičemž A5/1 je robustnější šifra orientovaná na hardware používaná v Evropě a A5/2 je záměrně oslabená verze pro export. A5/3, založená na blokové šifře Kasumi, byla zavedena pro zvýšené zabezpečení.

Z architektonického hlediska je A5/X aplikován v protokolové vrstvě odpovědné za správu rádiových zdrojů, konkrétně po kanálovém kódování a prokládání. Po aktivaci šifrování nařízené sítí se MS a BTS synchronizují pomocí stejného Kc a veřejně přenášeného čísla rámce (FN) k inicializaci algoritmu. To zajišťuje, že pro daný rámec je na obou koncích generován stejný šifrovací klíčový proud. Vnitřní stav algoritmu, typicky implementovaný pomocí posuvných registrů s lineární zpětnou vazbou (LFSR) u A5/1 a A5/2, je taktován nelineárním způsobem za použití FN a Kc. Výsledný šifrovací klíčový proud je pak aplikován na dávku dat v rámci tohoto TDMA rámce.

Klíčové komponenty zahrnují samotný šifrovací algoritmus, 64bitový šifrovací klíč (Kc), 22bitové číslo rámce a řídicí signalizaci pro nastavení šifrovacího režimu. Jeho role je výhradně pro šifrování přes vzdušné rozhraní na rozhraní Um (GSM) nebo Uu (pro doménu CS v raném UMTS), čímž poskytuje první obrannou linii proti odposlechu. Neposkytuje ochranu integrity, která byla přidána později v 3G s algoritmy UEA/UIA. Síla se výrazně liší: A5/0 nenabízí žádnou ochranu, A5/1 byla kryptograficky prolomena, ale vyžadovala značné úsilí, A5/2 byla triviálně slabá a A5/3 (Kasumi) byla považována za robustní, dokud se neobjevily pokročilejší útoky, což vedlo k jejímu postupnému vyřazení ve prospěch algoritmů založených na AES v pozdějších vydáních 3GPP.

## K čemu slouží

Algoritmy A5/X byly vytvořeny, aby řešily základní bezpečnostní zranitelnost analogových celulárních systémů, které byly náchylné k přímému odposlechu. S digitálním přechodem v GSM vznikla kritická potřeba zajistit základní důvěrnost pro hlasové a datové přenosy přes rádiovou cestu, která je nejvíce exponovanou částí sítě. Primárním řešeným problémem bylo zabránění běžnému odposlechu konverzací a signalizačních zpráv neoprávněnými stranami, čímž se budovala důvěra uživatelů v mobilní telefonii. Původní návrh usiloval o rovnováhu mezi výpočetní efektivitou pro omezený hardware raných mobilních telefonů a vnímanou adekvátní úrovní zabezpečení proti současným hrozbám.

Historicky byl vývoj ovlivněn exportními předpisy a politickými úvahami, což vedlo k vytvoření více variant. A5/1 byla určena pro použití v určitých regionech, zatímco A5/2 byla záměrně oslabená verze pro splnění exportních kontrol na silnou kryptografii. Tento dvojí přístup vytvořil fragmentované bezpečnostní prostředí. Omezení dřívějších A5/1 a A5/2 se výrazně projevila s pokrokem kryptografického výzkumu, který odhalil závažné nedostatky umožňující praktické útoky s mírným výpočetním výkonem. To motivovalo vývoj A5/3, založené na silnější blokové šifře Kasumi, k obnovení bezpečnostních záruk. Avšak hlavním omezením rodiny A5/X byla její závislost na 64bitovém klíči a u některých variant inherentně slabé návrhy, které se nakonec ukázaly jako nedostatečné proti státním aktérům a organizovanému zločinu, což vedlo k potřebě zcela nových kryptografických sad ve standardech 3G a 4G.

## Klíčové vlastnosti

- Návrh proudové šifry pro efektivní šifrování spojitých datových proudů přes rádiové dávky
- Více algoritmických variant (A5/0 až A5/7) nabízejících různé úrovně zabezpečení, včetně nulové šifry (A5/0)
- Používá 64bitový šifrovací klíč (Kc) odvozený z procesu autentizace
- Synchronizace pomocí veřejně přenášeného čísla TDMA rámce pro generování šifrovacího klíčového proudu
- Aplikován na fyzické vrstvě po kanálovém kódování pro hlasový a datový provoz GSM
- Poskytuje pouze důvěrnost, bez mechanismu ochrany integrity

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [A5/X na 3GPP Explorer](https://3gpp-explorer.com/glossary/a5-x/)
