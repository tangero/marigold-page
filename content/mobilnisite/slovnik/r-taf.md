---
slug: "r-taf"
url: "/mobilnisite/slovnik/r-taf/"
type: "slovnik"
title: "R-TAF – Reception side Terminal Adaptation Function"
date: 2025-01-01
abbr: "R-TAF"
fullName: "Reception side Terminal Adaptation Function"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/r-taf/"
summary: "Funkční entita definovaná pro služby s přepojováním okruhů (Circuit Switched) v 3GPP, která adaptuje datový proud přijímaný ze sítě pro prezentaci koncovému zařízení (TE). Provádí rychlostní adaptaci"
---

R-TAF je funkce adaptace terminálu na přijímací straně, která adaptuje přijímaný datový proud ze sítě pro koncové zařízení prováděním rychlostní adaptace a konverzí za účelem zajištění kompatibility.

## Popis

Funkce adaptace terminálu na přijímací straně (R-TAF) je funkce protokolové vrstvy definovaná ve specifikacích 3GPP pro služby dat s přepojováním okruhů ([CSD](/mobilnisite/slovnik/csd/)). Je umístěna v části mobilního ukončení ([MT](/mobilnisite/slovnik/mt/)) uživatelského zařízení (UE) nebo v samostatném adaptéru terminálu. Jejím hlavním úkolem je adaptovat datový proud přicházející ze strany sítě (z funkce pro vzájemné propojení, [IWF](/mobilnisite/slovnik/iwf/)) pro správné zpracování koncovým zařízením ([TE](/mobilnisite/slovnik/te/)), jako je například notebook nebo [PDA](/mobilnisite/slovnik/pda/) připojené přes sériový kabel. R-TAF pracuje ve spojení se svou protějškovou funkcí, [T-TAF](/mobilnisite/slovnik/t-taf/) (na vysílací straně), která provádí inverzní funkci pro směr uplink.

Provozně R-TAF provádí rychlostní adaptaci a další nezbytné protokolové konverze. V typickém datovém hovoru s přepojováním okruhů síť zřídí přenosový kanál s konkrétní rychlostí (např. standardní transparentní kanál 64 kbps nebo pomalejší netransparentní kanál). Aplikace na koncovém zařízení však může pracovat s jinou datovou rychlostí nebo používat jinou strukturu rámců. R-TAF řeší tento nesoulad. Pro netransparentní služby se účastní protokolu rádiového spoje ([RLP](/mobilnisite/slovnik/rlp/)), který poskytuje opravu chyb retransmisí poškozených rámců. R-TAF přijímá RLP rámce ze sítě, zpracovává je (např. potvrzuje správně přijaté rámce, žádá o retransmise chybných) a následně extrahuje datovou část uživatelských dat.

Po případném zpracování RLP provede R-TAF finální rychlostní adaptaci. Klíčovou standardní funkcí je rychlostní adaptace V.110, která převádí synchronní datový proud ze sítě (často o rychlosti 64, 56 nebo 48 kbps) na rychlost očekávanou sériovým rozhraním koncového zařízení (např. podle standardu V.24/RS-232). To zahrnuje bitové vkládání, synchronizaci a vytváření rámců. Adaptovaná data jsou následně předána koncovému zařízení přes fyzické rozhraní (např. referenční bod R). R-TAF je kritická komponenta v celé datové cestě, která zajišťuje, že navzdory možným rozdílům v datových rychlostech a protokolech mezi přenosovou službou mobilní sítě a koncovým uživatelským zařízením jsou data doručena příjemné aplikaci správně a kompletně.

## K čemu slouží

R-TAF byl vytvořen k řešení zásadní výzvy raných mobilních datových služeb: překlenutí propasti mezi standardizovanými synchronními přenosovými službami poskytovanými sítí s přepojováním okruhů a různorodými, často asynchronními rozhraními datových koncových zařízení, jako jsou notebooky a osobní digitální asistenty. V éře GSM a raného UMTS byly datové hovory zřizovány přes kanály s přepojováním okruhů, které poskytovaly pevný synchronní datový kanál. Spotřebitelská výpočetní technika však primárně používala standardní sériová rozhraní (RS-232/V.24) s proměnlivými, často nižšími podporovanými datovými rychlostmi.

Účelem funkce adaptace terminálu ([TAF](/mobilnisite/slovnik/taf/)), rozdělené na R-TAF (příjem) a T-TAF (vysílání), bylo poskytnout standardizovanou metodu pro rychlostní a protokolovou adaptaci. Bez ní by každé zařízení vyžadovalo proprietární adaptér. R-TAF konkrétně řeší problém na downlinkové cestě. Přijímá synchronní datový proud ze sítě, který může obsahovat rámce protokolu pro opravu chyb (RLP), a převádí jej do formátu a rychlosti vhodných pro připojené koncové zařízení. To umožňuje funkci plug-and-play pro datová zařízení používající standardní sériové kabely a modemy.

Historicky to bylo zásadní pro umožnění mobilního faxu, vytáčeného připojení k síti a raného přístupu k mobilnímu internetu. Představovalo klíčovou funkci pro vzájemné propojení, která umožňovala, aby se mobilní síť chovala jako modem pro standardní datové aplikace. R-TAF jako součást celkové funkce TAF poskytoval potřebnou flexibilitu pro podporu více přenosových rychlostí a možností terminálu, což byl klíčový faktor komerčního úspěchu datových služeb s přepojováním okruhů před rozšířeným nasazením služeb s přepojováním paketů (GPRS) a pozdějších datových služeb 3G/4G.

## Klíčové vlastnosti

- Provádí rychlostní adaptaci (např. V.110) na downlinkovém datovém proudu ze sítě k terminálu
- Zpracovává rámce protokolu rádiového spoje (RLP) pro netransparentní datové služby
- Převádí synchronní síťová data do formátu vhodného pro rozhraní koncového zařízení (TE)
- Funguje ve spojení s funkcí adaptace terminálu na vysílací straně (T-TAF) pro plně duplexní adaptaci
- Je umístěn v mobilním ukončení (MT) nebo v samostatném adaptéru terminálu
- Umožňuje kompatibilitu mezi přenosovými kanály sítě s přepojováním okruhů a standardním sériovým koncovým zařízením

## Definující specifikace

- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization

---

📖 **Anglický originál a plná specifikace:** [R-TAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/r-taf/)
