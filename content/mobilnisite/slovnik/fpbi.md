---
slug: "fpbi"
url: "/mobilnisite/slovnik/fpbi/"
type: "slovnik"
title: "FPBI – Fixed Part Beacon Identity"
date: 2025-01-01
abbr: "FPBI"
fullName: "Fixed Part Beacon Identity"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fpbi/"
summary: "Jedinečný identifikátor pro pevné části (základnové stanice) v celulárních systémech, používaný pro objevování sítě a synchronizaci. Umožňuje mobilním zařízením identifikovat a vybírat vhodnou pevnou"
---

FPBI (identita majáku pevné části) je jedinečný identifikátor základnové stanice pevné části, který mobilní zařízení používají pro objevování sítě, synchronizaci a výběr sítě za účelem podpory plynulého přechodu mezi buňkami.

## Popis

Fixed Part Beacon Identity (FPBI, identita majáku pevné části) je identifikátor definovaný ve specifikacích 3GPP, konkrétně v TS 43.052, pro pevné části ([FP](/mobilnisite/slovnik/fp/)) v celulárních sítích, zejména v kontextech jako systémy bezšňůrové telefonie (např. propojení [DECT](/mobilnisite/slovnik/dect/)/GSM) nebo pevný bezdrátový přístup. FPBI slouží jako majákový signál, který vysílá identitu pevné části, což umožňuje uživatelskému zařízení (UE) tuto FP detekovat, identifikovat a případně se na ni připojit. Je to klíčová součást procesů objevování sítě, výběru buňky a synchronizace.

Z architektonického hlediska FPBI vysílá pevná část přes rozhraní vzduchu jako součást svých majákových nebo pilotních signálů. Tento identifikátor je jedinečný v rámci určité administrativní domény (jako je síť operátora nebo geografická oblast) a UE jej používá k rozlišení různých FP. Když UE skenuje dostupné sítě, detekuje tyto majákové signály, dekóduje FPBI a použije jej k určení, zda je FP vhodná pro připojení na základě předkonfigurovaných preferencí nebo síťových politik. FPBI může mít hierarchickou strukturu a zahrnovat prvky jako kód síťového operátora, oblast umístění nebo typ FP.

FPBI funguje ve spojení s dalšími systémovými informacemi vysílanými pevnou částí. Po detekci majáku UE čte další parametry, jako jsou synchronizační kódy, informace o kanálu a přístupová práva. Samotný FPBI nenese bezpečnostní přihlašovací údaje, ale slouží jako veřejný štítek. Jeho hlavní rolí je usnadnit počáteční připojení a přechod mezi buňkami – například UE pohybující se v budově s více FP může použít FPBI k identifikaci nejlépe sloužící FP. V některých implementacích může být FPBI mapován na identity vyšších vrstev, jako je Cell Global Identity ([CGI](/mobilnisite/slovnik/cgi/)), nebo použit v službách založených na poloze.

Mezi klíčové komponenty patří vysílač pevné části, který vysílá FPBI, přijímač UE, který jej detekuje, a systémy správy sítě, které přiřazují a spravují hodnoty FPBI, aby se předešlo konfliktům. FPBI je nezbytný pro scénáře s hustým nasazením malých buněk nebo privátních sítí, kde je nutná jasná identifikace každého přístupového bodu. Podporuje funkce jako předávání hovoru, vyvažování zátěže a optimalizaci sítě tím, že poskytuje stabilní referenci pro identifikaci buňky.

## K čemu slouží

FPBI byl vytvořen, aby řešil potřebu jedinečné identifikace pevné infrastruktury v hybridních nebo více-dodavatelských celulárních sítích, zejména v bezšňůrové telefonii a raných systémech konvergence pevných a mobilních sítí. Před standardizovanými identifikátory, jako je FPBI, vedly proprietární schémata k problémům s interoperabilitou, což ztěžovalo UE plynulý roaming mezi zařízeními různých výrobců. FPBI poskytl jednotný způsob, jak mohou pevné části oznamovat svou přítomnost, a umožnil tak konzistentní objevování sítě v různorodých nasazeních.

Historicky, jak se celulární sítě rozšiřovaly o rezidenční základnové stanice, podnikové femtobuňky a propojení s bezšňůrovou telefonií, docházelo k rostoucímu množství pevných přístupových bodů. Správa těchto bodů vyžadovala jasný identifikační mechanismus, aby se předešlo zmatkům a zajistilo správné připojení UE. FPBI tento problém vyřešil tím, že nabídl standardizovaný formát identity, který mohl rozpoznat jakékoli kompatibilní UE. Také podpořil plánování sítě tím, že umožnil operátorům přiřazovat strukturované identity odrážející geografické nebo logické skupiny.

Motivace pro FPBI pramenila z touhy zlepšit uživatelský zážitek v prostředích s více překrývajícími se pokrytími, jako jsou kancelářské budovy nebo domácnosti s několika bezšňůrovými telefony. Řešil omezení používání pouze rádiové frekvence nebo čísel kanálů pro identifikaci, které byly v hustých nasazeních nedostatečné. Poskytnutím jedinečné identity majáku FPBI umožnil rychlejší hledání buňky, snížil ping-pong efekt během přechodu mezi buňkami a usnadnil pokročilé funkce, jako je výběr preferovaného přístupového bodu. Položil základy pro pozdější identifikátory malých buněk v LTE a 5G.

## Klíčové vlastnosti

- Jedinečný identifikátor vysílaný pevnými částmi (základnovými stanicemi)
- Používaný UE pro objevování sítě a výběr buňky
- Podporuje synchronizaci a procedury počátečního přístupu
- Umožňuje přechod mezi body pevné infrastruktury
- Usnadňuje správu a plánování sítě
- Standardizovaný formát pro interoperabilitu mezi dodavateli

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 43.052** (Rel-19) — GSM Cordless Telephony System (CTS) Radio Interface

---

📖 **Anglický originál a plná specifikace:** [FPBI na 3GPP Explorer](https://3gpp-explorer.com/glossary/fpbi/)
