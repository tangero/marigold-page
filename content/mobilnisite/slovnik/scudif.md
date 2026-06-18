---
slug: "scudif"
url: "/mobilnisite/slovnik/scudif/"
type: "slovnik"
title: "SCUDIF – Service Change and UDI/RDI Fallback"
date: 2025-01-01
abbr: "SCUDIF"
fullName: "Service Change and UDI/RDI Fallback"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/scudif/"
summary: "SCUDIF je mechanismus služby 3GPP, který spravuje změny služeb a poskytuje návrat (fallback) k přenosovým službám Unrestricted Digital Information (UDI) nebo Restricted Digital Information (RDI). Zaji"
---

SCUDIF je mechanismus služby 3GPP, který spravuje změny služeb a poskytuje návrat (fallback) k přenosovým službám UDI nebo RDI, aby byla zajištěna kontinuita služby, pokud nelze podporovat požadovanou službu.

## Popis

Service Change and [UDI](/mobilnisite/slovnik/udi/)/[RDI](/mobilnisite/slovnik/rdi/) Fallback (SCUDIF) je schopnost síťové služby definovaná v architektuře 3GPP, primárně dokumentovaná ve specifikacích jako TS 23.018 a TS 23.172. Funguje v rámci jádra sítě, konkrétně se zapojením Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) a Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)), pro řešení scénářů, kdy nelze navázat požadovanou přenosovou službu nebo teleslužbu tak, jak bylo původně zamýšleno. Mechanismu se využívá během procedur sestavování hovoru nebo změny služby. Když síť zjistí, že požadovaná služba (např. specifická datová rychlost nebo multimediální služba) není k dispozici kvůli schopnostem terminálu, přetížení sítě nebo předávání mezi systémy, SCUDIF spustí proceduru návratu (fallback). Tato procedura se pokusí navázat alternativní, typicky základnější přenosovou službu. Návrat cílí buď na přenosovou službu Unrestricted Digital Information (UDI), která podporuje transparentní přenos dat, nebo na službu Restricted Digital Information (RDI), často používanou pro faxové služby. Výběr mezi UDI a RDI je založen na původní žádosti o službu a síťových politikách.

Architektonická role SCUDIF je nedílnou součástí vyjednávání služeb a správy mobility. Interaguje s protokoly jako [BSSAP](/mobilnisite/slovnik/bssap/) (Base Station System Application Part) a [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part) pro komunikaci rozhodnutí o změně služby mezi MSC, GMSC a rádiovou přístupovou sítí. Mezi klíčové zapojené komponenty patří funkce řízení hovoru v rámci MSC, která vyhodnocuje kompatibilitu služeb, a mezifunkční jednotky, které přizpůsobují parametry přenosové služby. SCUDIF je obzvláště důležitý v legacy okruzově komutovaných doménách, zajišťuje, že hovory nejsou při nedostupnosti pokročilých služeb okamžitě neúspěšné, a tím zlepšuje míru dokončení hovorů a uživatelský zážitek.

Při provozu SCUDIF následuje definovanou sekvenci. Po přijetí žádosti o službu síť provede kontrolu kompatibility. Pokud je zjištěna nekompatibilita, MSC může iniciovat oznámení o změně služby volající a volané straně, což indikuje úpravu schopnosti přenosu. Následně se pokusí navázat návratové spojení pomocí parametrů UDI nebo RDI. Tento proces může zahrnovat vyjednávání se vzdáleným koncem a potenciálně úpravu provozního kanálu v rádiové přístupové síti. Role SCUDIF se rozšiřuje na scénáře předávání mezi GSM a dalšími systémy (jako je [PSTN](/mobilnisite/slovnik/pstn/)), kde musí být zachována kontinuita služby navzdory odlišné podpoře služeb. Jeho implementace zajišťuje zpětnou kompatibilitu a hladkou spolupráci mezi síťovými prvky s různými schopnostmi, což je základním kamenem robustního návrhu telekomunikačních služeb.

## K čemu slouží

SCUDIF byl zaveden pro řešení kritických problémů interoperability služeb a dokončování hovorů v heterogenních a vyvíjejících se mobilních sítích. V raných fázích nasazení GSM a UMTS podporovaly sítě a uživatelská zařízení širokou škálu přenosových služeb a teleslužeb, od základního hlasu po různé datové služby. Ne všechny síťové uzly nebo účastnické terminály však podporovaly každou pokročilou službu. Bez mechanismu návratu by hovor nebo relace žádající o nepodporovanou službu jednoduše selhaly, což by vedlo ke špatnému uživatelskému zážitku a neefektivnímu využívání síťových zdrojů. SCUDIF byl vytvořen, aby toto vyřešil, a to poskytnutím standardizované procedury pro plynulý přechod na běžně podporovanou základní digitální přenosovou službu (UDI nebo RDI), což zajišťuje, že hovor může pokračovat, i když s potenciálně sníženými schopnostmi.

Historický kontext spočívá v přechodu z analogových na digitální celulární systémy a v zavádění doplňkových služeb. Jak 3GPP Release 99 a následující verze rozšiřovaly nabídku služeb, potřeba robustního vyjednávání služeb se stala prvořadou. Předchozí přístupy se často spoléhaly na statické profily služeb nebo vedly k přerušení hovoru, což bylo pro komerční telefonii nepřijatelné. SCUDIF formalizoval dynamický proces návratu, který umožňuje sítím přizpůsobit se omezením ve schopnostech terminálů, přetížení sítě nebo předávání mezi systémy (např. do PSTN sítě, která podporuje pouze základní digitální služby). To bylo obzvláště důležité pro usnadnění roamingu a propojení mezi operátory, kde se podpora služeb mohla výrazně lišit.

Řešením těchto omezení SCUDIF zvýšil spolehlivost sítě a spokojenost uživatelů. Umožnil operátorům zavádět nové služby postupně, aniž by přerušovali stávající hovory, čímž podpořil plynulejší cestu vývoje. Mechanismus také hrál roli v optimalizaci síťových zdrojů tím, že zabraňoval zbytečným selháním při sestavování hovoru a následným opětovným pokusům, čímž zlepšil celkovou efektivitu sítě a dostupnost služeb.

## Klíčové vlastnosti

- Dynamické zahájení změny služby během sestavování nebo úpravy hovoru
- Návrat (fallback) k přenosové službě Unrestricted Digital Information (UDI)
- Návrat (fallback) k přenosové službě Restricted Digital Information (RDI)
- Integrace s funkcemi řízení hovoru v MSC a GMSC
- Podpora scénářů předávání mezi systémy
- Standardizované procedury napříč specifikacemi 3GPP pro interoperabilitu

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.172** (Rel-19) — Service Change and UDI Fallback (SCUDIF)
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification

---

📖 **Anglický originál a plná specifikace:** [SCUDIF na 3GPP Explorer](https://3gpp-explorer.com/glossary/scudif/)
