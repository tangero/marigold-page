---
slug: "apm"
url: "/mobilnisite/slovnik/apm/"
type: "slovnik"
title: "APM – Application Transport Mechanism / Application Transport Message"
date: 2025-01-01
abbr: "APM"
fullName: "Application Transport Mechanism / Application Transport Message"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/apm/"
summary: "APM je protokolový mechanismus 3GPP pro přenos aplikačních dat, například signalizace doplňkových služeb, přes IP sítě. Umožňuje doručování informací specifických pro služby mezi síťovými entitami a z"
---

APM je protokolový mechanismus 3GPP pro přenos aplikačních dat, například signalizace doplňkových služeb, přes IP sítě mezi síťovými entitami.

## Popis

Mechanismus pro přenos aplikací (Application Transport Mechanism, APM) je protokolový rámec definovaný ve specifikacích 3GPP, který usnadňuje přenos zpráv aplikační vrstvy, zejména těch souvisejících s doplňkovými službami a dalšími telefonními aplikacemi, přes rozhraní založená na IP. Funguje jako adaptační vrstva nad standardními transportními protokoly, jako jsou TCP nebo SCTP, a poskytuje strukturovanou obálku pro zapouzdření dat specifických pro aplikaci. Hlavní entitou APM je zpráva pro přenos aplikací (Application Transport Message), která obsahuje hlavičku s informacemi o směrování a rozlišení protokolu, následovanou vlastní datovou jednotkou aplikace. Tato struktura umožňuje přijímacím uzlům správně identifikovat zdrojovou aplikaci a zprávu podle toho zpracovat, což umožňuje bezproblémovou spolupráci mezi různými síťovými prvky a servisními platformami.

Architektonicky se APM používá na rozhraních, jako je rozhraní Mc mezi řadičem mediální brány ([MGC](/mobilnisite/slovnik/mgc/)) a mediální bránou ([MGW](/mobilnisite/slovnik/mgw/)) v subsystému IP multimédií (IMS) 3GPP a při vývoji jádrové sítě s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)). Funguje jako součást zásobníku protokolu H.248/Megaco, kde přenáší balíčky obsahující specifické aplikační kontexty, například data doplňkových služeb definovaná v 3GPP 29.232. Mechanismus definuje postupy pro sestavení, přenos a rozebrání zprávy, čímž zajišťuje zachování sémantiky aplikační vrstvy přes transportní spojení. Mezi klíčové komponenty patří formát zprávy APM, identifikační pole pro typy aplikací a mechanismy pro zpracování chyb, které zaručují spolehlivé doručení.

Při provozu zdrojová aplikační entita, například funkce přepojování služeb, naformátuje svá data podle příslušného aplikačního protokolu. Tato data jsou následně zapouzdřena do zprávy APM, která přidá potřebné informace o adresování na transportní vrstvě a rozlišení protokolu. Zpráva je odeslána přes IP transportní spojení do cílového uzlu. Po přijetí cíl vyjme užitečná data APM, použije rozlišovač protokolu k určení aplikačního kontextu a předá vnitřní data příslušnému zpracovateli. Tím se oddělí aplikační logika od podrobností podkladového transportu, čímž se poskytuje flexibilní a standardizovaný přenosový mechanismus.

Úlohou APM v síti je podpora migrace od tradiční signalizace založené na TDM k plně IP architekturám při zachování zpětné kompatibility pro základní telefonní služby. Zajišťuje, že signalizace doplňkových služeb – jako přesměrování hovoru, zákazy nebo identifikace linky – může být spolehlivě přenášena mezi síťovými uzly, které mohou být implementovány různými dodavateli. Tím, že poskytuje společný přenosový prostředek pro různé aplikační protokoly, APM snižuje složitost integrace a podporuje interoperabilitu v síťových prostředích s více dodavateli a více generacemi.

## K čemu slouží

APM byl vytvořen, aby řešil výzvu přenosu signalizace starších telefonních aplikací s přepojováním okruhů přes paketové IP sítě během vývoje sítí 3GPP počínaje Release 99. Před jádrovými sítěmi založenými na IP se signalizace doplňkových služeb přenášela přes vyhrazené TDM časové sloty nebo signalizační spoje SS7, které byly těsně svázány s infrastrukturou s přepojováním okruhů. Přechod k plně IP jádru, motivovaný snížením nákladů a větší flexibilitou, vyžadoval mechanismus pro zapouzdření a doručení těchto dat aplikační vrstvy přes obecné IP transportní protokoly bez ztráty funkčnosti služeb.

Hlavní problém, který APM řeší, je interoperabilita mezi novými síťovými prvky založenými na IP a starší servisní logikou. Bez standardizovaného transportního mechanismu by každý dodavatel nebo služba mohl implementovat vlastní metody zapouzdření, což by vedlo k fragmentaci a problémům s integrací. APM poskytuje jednotnou obálku, která může přenášet různé aplikační protokoly, což umožňuje operátorům nasazovat IP mediální brány a řadiče při zachování stávajících doplňkových služeb. To bylo obzvláště kritické pro plynulý přechod ze sítí 2G/3G [CS](/mobilnisite/slovnik/cs/) k architektuře IMS, což zajišťovalo kontinuitu služeb pro koncové uživatele.

Historicky vycházela motivace z práce 3GPP na jádrové síti nezávislé na přenosu ([BICN](/mobilnisite/slovnik/bicn/)) a oddělení řídicí a přenosové roviny. Jak je specifikováno ve standardech jako 23.153 a 29.205, APM umožnil protokolu H.248 přenášet balíčky specifické pro 3GPP mezi řadičem mediální brány a mediální bránou. Řešil omezení nativního mechanismu balíčků H.248, který původně nebyl navržen pro specifické požadavky signalizace doplňkových služeb 3GPP, přidáním specializované transportní vrstvy šité na míru těmto aplikačním zprávám.

## Klíčové vlastnosti

- Standardizované zapouzdření signalizačních dat aplikační vrstvy přes IP transport
- Pole pro rozlišení protokolu k identifikaci specifického aplikačního kontextu (např. doplňkové služby 3GPP)
- Integrace se zásobníkem protokolu H.248/Megaco pro řízení mediální brány
- Podpora spolehlivého přenosu prostřednictvím podkladových protokolů jako TCP nebo SCTP
- Umožňuje interoperabilitu mezi síťovými prvky od více dodavatelů v plně IP jádrech
- Usnadňuje zpětnou kompatibilitu pro starší telefonní služby během migrace sítě

## Související pojmy

- [MEGACO – MEdia GAteway COntrol](/mobilnisite/slovnik/megaco/)

## Definující specifikace

- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2
- **TS 23.284** (Rel-19) — Local Call Local Switch Stage 2
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.205** (Rel-19) — BICC Protocols for Bearer-Independent CS Core Network
- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking

---

📖 **Anglický originál a plná specifikace:** [APM na 3GPP Explorer](https://3gpp-explorer.com/glossary/apm/)
