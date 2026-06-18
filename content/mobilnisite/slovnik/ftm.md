---
slug: "ftm"
url: "/mobilnisite/slovnik/ftm/"
type: "slovnik"
title: "FTM – Frame Tunnelling Mode"
date: 2025-01-01
abbr: "FTM"
fullName: "Frame Tunnelling Mode"
category: "Protocol"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ftm/"
summary: "Provozní režim funkce adaptace terminálu (Terminal Adaptation Function – TAF) v 3GPP, který umožňuje transparentní tunelování kompletních rámců vrstvy datového spoje mezi mobilním terminálem (Mobile T"
---

FTM je režim TAF, který umožňuje transparentní tunelování kompletních rámců datového spoje mezi mobilním terminálem (Mobile Terminal) a mezifunkční jednotkou (Interworking Function) za účelem podpory starších datových služeb v sítích UMTS.

## Popis

Frame Tunnelling Mode (FTM) je specifický provozní režim definovaný pro funkci adaptace terminálu (Terminal Adaptation Function – [TAF](/mobilnisite/slovnik/taf/)) v rámci protokolové architektury 3GPP. Jeho hlavní funkcí je umožnit podporu datových služeb nepocházejících z 3GPP, konkrétně služeb GSM Circuit Switched Data ([CSD](/mobilnisite/slovnik/csd/)) a General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)), přes rádiový přístupový síť UMTS a její core network. FTM funguje tak, že zapouzdřuje kompletní rámce vrstvy datového spoje (např. LAPDm rámce pro GSM data) z koncového zařízení (Terminal Equipment – [TE](/mobilnisite/slovnik/te/)) a transparentně je přenáší mezi mobilní částí (Mobile Termination – [MT](/mobilnisite/slovnik/mt/)) v uživatelském zařízení (UE) a mezifunkční jednotkou (Interworking Function – [IWF](/mobilnisite/slovnik/iwf/)) v síti.

Z architektonického hlediska se TAF nachází v MT. Při práci v režimu FTM TAF neinterpretuje ani nezpracovává protokoly vrstvy datového spoje z TE. Místo toho funguje jako průchozí prvek, který přebírá nezpracované rámce ze sériového rozhraní TE (pomocí AT příkazů definovaných v TS 27.007) a zabalí je pro přenos přes UMTS spojení. Tyto rámce jsou transparentně přenášeny sítí UMTS pomocí Radio Access Bearer ([RAB](/mobilnisite/slovnik/rab/)) pro circuit-switched spojení nebo příslušných přenosových kanálů pro packet-switched spojení. IWF, umístěná na hranici sítě (často u [MSC](/mobilnisite/slovnik/msc/) nebo SGSN), přijme tunelované rámce, extrahuje původní LAPDm rámec a zpracuje jej, jako by pocházel přímo z GSM MS. To umožňuje core networku transparentně poskytovat starší GSM datovou službu.

Klíčem pro fungování FTM je použití signalizace v pásmu (in-band) uvnitř tunelovaného datového proudu pro správu datového spojení. Příkazy jako navázání, udržování a uvolnění datového spoje jsou přenášeny uvnitř samotných tunelovaných rámců, nikoli signalizační vrstvou UMTS. Tento režim je klíčový pro zpětnou kompatibilitu, protože umožňuje dvoupásmovým terminálům GSM/UMTS poskytovat konzistentní datové služby bez ohledu na podkladovou rádiovou technologii, aniž by to vyžadovalo změny v koncovém zařízení (např. v laptopu s GSM datovou kartou).

## K čemu slouží

FTM byl vytvořen k vyřešení kritického problému kontinuity služeb a zpětné kompatibility během přechodu ze sítí GSM/GPRS na UMTS (3G). Nové UMTS terminály potřebovaly podporovat stávající, široce rozšířené GSM datové služby, jako je Circuit Switched Data (pro fax, vytáčené připojení) a GPRS, aniž by uživatelé museli měnit své koncové zařízení (TE) nebo aplikace. Motivací bylo zajistit bezproblémový uživatelský zážitek a chránit investice operátorů do stávající servisní infrastruktury.

Tato technologie řeší omezení přístupu přímého protokolového překladu. Překlad protokolů GSM LAPDm na protokoly UMTS by byl složitý a nemusel by podporovat všechny funkce nebo rozšíření specifická pro dodavatele. Transparentní tunelování FTM tento problém elegantně obchází tím, že s GSM datovým spojem zachází jako s datovou náplní. Síť UMTS jednoduše poskytuje přenosový kanál a stávající síťové prvky GSM (IWF) na okraji core networku zpracovávají známé protokoly. Tento návrh minimalizoval změny potřebné jak v terminálu, tak v core networku pro základní propojení datových služeb.

Historicky byl FTM nezbytný pro raná nasazení 3G, kde bylo pokrytí nesouvislé a terminály často přepínaly mezi GSM a UMTS. Umožňoval předávání datových relací mezi těmito technologiemi bez přerušení logického datového spojení, jak jej vnímalo TE. Jeho specifikace v TS 27.001 a TS 29.007 poskytla potřebné podrobnosti pro výrobce terminálů a sítí, aby tuto schopnost vzájemného propojení implementovali konzistentně, což usnadnilo hladké zavedení služeb 3G.

## Klíčové vlastnosti

- Transparentní tunelování kompletních rámců vrstvy datového spoje (např. LAPDm)
- Umožňuje služby GSM Circuit Switched Data a GPRS přes přístup UMTS
- Funguje jako režim funkce adaptace terminálu (Terminal Adaptation Function – TAF)
- Používá signalizaci v pásmu (in-band) uvnitř tunelovaných dat pro řízení spoje
- Vyžaduje v síti mezifunkční jednotku (Interworking Function – IWF) pro ukončení tunelu
- Poskytuje kontinuitu služeb a zpětnou kompatibilitu pro dvoupásmové terminály

## Související pojmy

- [TAF – Terminal Adaptation Function](/mobilnisite/slovnik/taf/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TS 27.001** (Rel-19) — Terminal Adaptation Functions for PLMN
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 29.007** (Rel-19) — PLMN-PSTN/ISDN Interworking Requirements

---

📖 **Anglický originál a plná specifikace:** [FTM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ftm/)
