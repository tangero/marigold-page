---
slug: "bicn"
url: "/mobilnisite/slovnik/bicn/"
type: "slovnik"
title: "BICN – Bearer Independent Core Network"
date: 2025-01-01
abbr: "BICN"
fullName: "Bearer Independent Core Network"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bicn/"
summary: "BICN je architektonický koncept 3GPP, který odděluje jádrovou síť od specifických podkladových transportních technologií a umožňuje tak jednotné jádro podporující více přístupových sítí, jako jsou GSM"
---

BICN je architektonický koncept 3GPP, který odděluje jádrovou síť od specifických transportních technologií, aby umožnil jednotné jádro podporující více přístupových sítí, jako jsou GSM, UMTS a LTE.

## Popis

Bearer Independent Core Network (BICN, jádrová síť nezávislá na přenosové technologii) je základní architektonický princip ve standardech 3GPP, který definuje strukturu jádrové sítě (CN) nezávislou na konkrétní rádiové přístupové technologii a jejích přidružených přepojovaných okruhů ([CS](/mobilnisite/slovnik/cs/)) nebo paketů ([PS](/mobilnisite/slovnik/ps/)). Jeho hlavním cílem je vytvořit jednotnou vrstvu jádrové sítě, která může obsluhovat více rádiových přístupových sítí (RAN), jako je GSM [EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), UMTS Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)) a později vyvinutý UTRAN ([E-UTRAN](/mobilnisite/slovnik/e-utran/) pro LTE), aniž by byla vázána na jejich nativní transportní mechanismy. Toho je dosaženo abstrakcí funkcí jádrové sítě od podkladových přenosových služeb, kdy je přístupová síť primárně považována za zdroj IP paketů nebo konektivní kanál. Architektura zdůrazňuje jasné oddělení řídicí roviny (signalizace) a uživatelské roviny (datový provoz), což je předchůdce formalizovanějšího oddělení řídicí a uživatelské roviny (CUPS) v pozdějších vydáních.

V jádru BICN využívá IP Multimedia Subsystem (IMS) jako primární platformu pro poskytování služeb pro multimediální služby v reálném čase, což znamená odklon od tradiční telefonie s přepojováním okruhů. Uzly jádrové sítě, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN), se vyvíjejí tak, aby podporovaly IP transport pro signalizaci i uživatelská data. Například MSC se může vyvinout v MSC Server (pro řízení) a Media Gateway (MGW) pro provoz v uživatelské rovině, propojené standardizovanými rozhraními, jako je rozhraní Mc (s použitím protokolů jako H.248). Podobně SGSN a Gateway GPRS Support Node (GGSN) využívají plně IP rozhraní Gn a Gp. To umožňuje, aby jediné, konsolidované jádro s přepojováním paketů zpracovávalo hlasové (prostřednictvím Voice over IP v IMS), video a datové služby bez ohledu na to, zda je uživatel připojen přes GSM, UMTS nebo LTE.

Klíčovými architektonickými prvky BICN jsou použití IP jako univerzální transportní vrstvy a definice propojovacích funkcí (IWFs) a mediálních bran pro zpracování provozu ze starších sítí s přepojováním okruhů. IMS poskytuje řízení komunikačních relací a aplikační servery pro servisní logiku, zatímco jádrová síť nezávislá na přenosové technologii zajišťuje transport a správu mobility. Tato architektura snižuje provozní složitost tím, že umožňuje operátorům spravovat jedinou, konvergovanou jádrovou síť pro všechny typy přístupu, čímž zjednodušuje rozšiřování sítě a nasazování služeb. Tvoří evoluční základ pro plně IP Evolved Packet Core (EPC) v 4G a 5G Core (5GC), které plně realizují vizi architektury nezávislé na přenosové technologii a založené na službách.

## K čemu slouží

BICN bylo zavedeno, aby řešilo rostoucí složitost a náklady na provoz více, oddělených jádrových sítí pro různé generace rádiových přístupových technologií (2G GSM, 3G UMTS). Před BICN museli operátoři udržovat paralelní jádrové sítě s přepojováním okruhů pro hlas a SMS a jádrové sítě s přepojováním paketů pro data, každá se svými specifickými uzly, rozhraními a transportními sítěmi. To vedlo k vysokým kapitálovým a provozním výdajům, neefektivnímu využívání zdrojů a pomalému nasazování služeb napříč různými přístupovými sítěmi. Odvětví potřebovalo cestu ke konsolidaci síťové infrastruktury a zjednodušení zavádění nových multimediálních služeb.

Hnací motivací byl přechod na plně IP sítě. Jak datové služby rostly a IP se stalo všudypřítomným protokolem pro komunikaci, 3GPP definovalo BICN, aby umožnilo jedinou, IP jádrovou síť schopnou podporovat všechny služby – hlas, video a data – přes jakoukoli přístupovou technologii. Tím se vyřešil problém služebních sil, kdy například služba jako videohovor mohla fungovat na 3G, ale ne na 2G. Tím, že se jádrová síť stala 'nezávislou na přenosové technologii', umožnilo operátorům flexibilně vyvíjet své sítě, znovu využívat jádrové prostředky při současném upgradu rádiového přístupu. Zároveň to pozicovalo IMS jako budoucí servisní vrstvu, zajišťující dlouhou životnost sítě a připravující cestu pro konvergenci pevných a mobilních sítí.

Historicky BICN poskytlo klíčový architektonický most od dvoudoménových sítí 2G/3G k ploché, plně IP architektuře 4G LTE/EPC. Řešilo omezení těsného propojení mezi rádiovými přenosovými technologiemi a protokoly jádrové sítě, což umožnilo efektivnější směrování provozu, zjednodušenou správu sítě a ekonomické výhody jednotné transportní a servisní platformy. Tento koncept byl zásadní pro zkrácení doby uvedení nových IP služeb na trh a pro správu souběžné existence starších a novějších generací přístupu během dlouhých migračních období.

## Klíčové vlastnosti

- Odděluje funkce jádrové sítě od specifických rádiových přístupových technologií (GERAN, UTRAN)
- Umožňuje jednotnou, IP jádrovou síť pro více typů přístupu
- Usnadňuje jasné oddělení funkcí řídicí a uživatelské roviny
- Podporuje poskytování služeb prostřednictvím IP Multimedia Subsystem (IMS) pro multimédia
- Využívá mediální brány a propojovací funkce pro kompatibilitu se staršími sítěmi s přepojováním okruhů
- Snižuje provozní složitost a náklady prostřednictvím konsolidace sítě

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TR 23.977** (Rel-19) — Bandwidth/Resource Savings & Speech Quality Requirements

---

📖 **Anglický originál a plná specifikace:** [BICN na 3GPP Explorer](https://3gpp-explorer.com/glossary/bicn/)
