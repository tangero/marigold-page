---
slug: "tch-hs"
url: "/mobilnisite/slovnik/tch-hs/"
type: "slovnik"
title: "TCH-HS – Traffic Channel Half rate Speech"
date: 2025-01-01
abbr: "TCH-HS"
fullName: "Traffic Channel Half rate Speech"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tch-hs/"
summary: "GSM provozní kanál přenášející řeč kódovanou poloviční přenosovou rychlostí, který efektivně zdvojnásobuje kapacitu sítě tím, že umožňuje dvěma hovorovým spojením sdílet jeden fyzický časový slot. Pou"
---

TCH-HS je GSM provozní kanál (Traffic Channel) přenášející řeč kódovanou poloviční přenosovou rychlostí, který umožňuje sdílení jednoho časového slotu dvěma hovorovým spojením za účelem zvýšení kapacity sítě na úkor určitého snížení kvality hlasu.

## Popis

TCH-HS (Traffic Channel Half rate Speech) je logický provozní kanál v systému GSM navržený ke zvýšení kapacity rádiového přístupového subsystému pro hlasové služby. Funguje tak, že využívá řečový kodek, který komprimuje hlas na přibližně poloviční datový tok oproti kodeku pro plnou rychlost, typicky kolem 5,6 kbps pro původní GSM Half Rate ([HR](/mobilnisite/slovnik/hr/)) kodek. To umožňuje multiplexovat dva samostatné TCH-HS kanály, a tedy dvě simultánní hovorová spojení, do jednoho fyzického časového slotu v rámci [TDMA](/mobilnisite/slovnik/tdma/) rámce. Tento [multiplexing](/mobilnisite/slovnik/multiplexing/) je dosažen pomocí subkanalizace, kdy je časový slot rozdělen na dva podslotty, z nichž každý je přiřazen jiné mobilní stanici. Podobně jako [TCH-FS](/mobilnisite/slovnik/tch-fs/) funguje TCH-HS v rámci 26-rámcové multirámcové struktury, ale alokace rámců pro provoz a přidruženého pomalu asociovaného řídicího kanálu ([SACCH](/mobilnisite/slovnik/sacch/)) je přizpůsobena pro dva subkanály.

Z pohledu technického provozu, když se síť rozhodne přidělit kanál s poloviční rychlostí – často na základě zatížení provozem a algoritmů optimalizace zdrojů – nakonfiguruje fyzický kanál v režimu poloviční rychlosti. Mobilní stanice i síťový transkodér ([TRAU](/mobilnisite/slovnik/trau/)) musí podporovat kodek pro poloviční rychlost. Řečový signál je zakódován s nižším datovým tokem a výsledný bitový proud je namapován na přidělený podslott. Dva subkanály na stejném časovém slotu jsou pečlivě synchronizovány, aby se předešlo interferenci. Každý subkanál má své vlastní asociované signalizační informace, přičemž SACCH informace pro každé spojení jsou přenášeny ve vyhrazených rámcích v rámci multirámce, což zajišťuje, že obě spojení mohou hlásit měření signálu a přijímat potřebné řídicí příkazy.

Z architektonického hlediska je TCH-HS spravován řadičem [BSC](/mobilnisite/slovnik/bsc/), který rozhoduje o použití poloviční rychlosti na základě konfigurace buňky a aktuálního zatížení. Jeho zavedení vyžadovalo vylepšení v základnové stanici [BTS](/mobilnisite/slovnik/bts/) pro zpracování subkanálů a v TRAU pro podporu kodeku poloviční rychlosti. Role TCH-HS je primárně o zvýšení kapacity. Umožňuje operátorům sítí obsloužit více účastníků se stejným množstvím rádiového spektra, což je klíčový ekonomický a provozní faktor. To však přichází za cenu potenciálně snížené kvality hlasu ve srovnání s kanálem plné rychlosti, protože kodek s nižším datovým tokem je náchylnější k audio artefaktům, zejména v hlučném prostředí. Použití TCH-HS je proto často dynamicky řízeno, s možností přechodu spojení na plnou rychlost, pokud kvalita degraduje nebo síťové zatížení poklesne.

## K čemu slouží

TCH-HS byl vyvinut k řešení kritického problému omezeného rádiového spektra a rostoucí poptávky po mobilních hlasových službách v 90. letech 20. století. Jeho primárním účelem je zvýšit kapacitu GSM sítě bez nutnosti dalších rádiových nosičů nebo lokalit buněk. Tím, že umožňuje dvěma spojením sdílet jeden fyzický zdroj, efektivně zdvojnásobuje hlasovou kapacitu na časový slot, což představuje významné zlepšení spektrální účinnosti. Tím se vyřešila ekonomická a technická výzva přetížení sítě v oblastech s vysokým provozem.

Motivace vycházela z úspěchu GSM a rychlého růstu počtu účastníků. Pevné přidělování jednoho časového slotu na spojení v modelu TCH-FS se stávalo úzkým hrdlem. TCH-HS představil kompromis: přijmout snížení kvality řeči (použitím kodeku s nižším datovým tokem a vyšší kompresí) výměnou za obsloužení většího počtu uživatelů. Šlo o pragmatické řešení pro operátory čelící kapacitním omezením. Řešilo to limit nepružného využití zdrojů u TCH-FS a poskytlo nástroj pro statistický multiplexing hlasového provozu. Nasazení TCH-HS bylo klíčovým krokem v optimalizaci využití sítě a oddálení nákladných rozšíření infrastruktury.

## Klíčové vlastnosti

- Přenos řeči poloviční přenosovou rychlostí (např. ~5,6 kbps pro GSM HR)
- Dvě nezávislá hovorová spojení multiplexovaná do jednoho fyzického časového slotu prostřednictvím subkanálů
- Využívá 26-rámcový multirámec přizpůsobený pro provoz s dvojitými subkanály
- Dynamicky přidělitelný sítí na základě potřeb kapacity
- Obsahuje nezávislou SACCH signalizaci pro každý subkanál
- Zdvojnásobuje teoretickou hlasovou kapacitu ve srovnání s TCH-FS na stejném spektru

## Související pojmy

- [TCH-FS – Traffic Channel Full rate Speech](/mobilnisite/slovnik/tch-fs/)
- [TCH/AFS – Traffic Channel for Adaptive Multi-Rate Full Rate Speech](/mobilnisite/slovnik/tch-afs/)
- [SACCH – Standalone Associated Control CHannel](/mobilnisite/slovnik/sacch/)

## Definující specifikace

- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [TCH-HS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tch-hs/)
