---
slug: "wim"
url: "/mobilnisite/slovnik/wim/"
type: "slovnik"
title: "WIM – Wireless Identity Module"
date: 2025-01-01
abbr: "WIM"
fullName: "Wireless Identity Module"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wim/"
summary: "Zabezpečená hardwarová nebo softwarová komponenta, která ukládá identitu účastníka (IMSI), autentizační klíče a síťové aplikace pro 3GPP mobilní zařízení. Je to obecný termín zahrnující fyzické SIM ka"
---

WIM je obecný 3GPP termín pro zabezpečenou komponentu, která ukládá identitu a klíče účastníka, provádí autentizaci a zahrnuje fyzické SIM, eSIM a iSIM.

## Popis

Wireless Identity Module (WIM) je zabezpečený prvek ve vybavení uživatele (UE) zodpovědný za hostování identity účastníka a kritických přihlašovacích údajů pro přístup k 3GPP sítím (GSM, UMTS, LTE, NR). Jedná se o odolné komponenty proti neoprávněné manipulaci, historicky o výměnné plastové karty (UICC se [SIM](/mobilnisite/slovnik/sim/) aplikací), které se vyvíjejí ve směru vnořeného hardwaru (eUICC) nebo integrovaného zabezpečeného prostředí (iUICC). Primární funkcí WIM je bezpečné uložení mezinárodního identifikátoru mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)) a dlouhodobého tajného klíče (K), které poskytuje operátor mobilní sítě. Také hostí aplikaci pro autentizaci a dohodu klíčů (např. SIM pro GSM, [USIM](/mobilnisite/slovnik/usim/) pro 3G/4G/5G, [ISIM](/mobilnisite/slovnik/isim/) pro IMS), která obsahuje kryptografické algoritmy (např. Milenage, TUAK).

Z architektonického hlediska WIM komunikuje s modemem UE prostřednictvím standardizovaného elektrického a logického rozhraní (např. [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 7816 pro fyzické karty nebo novější rozhraní pro vnořené formy). Když se UE pokouší připojit k síti, síť odešle do UE náhodnou výzvu ([RAND](/mobilnisite/slovnik/rand/)). Modem tuto výzvu předá WIM. USIM aplikace WIM použije uložený tajný klíč (K) a RAND jako vstupy do autentizačního algoritmu pro výpočet dvou kritických hodnot: odpovědi ([RES](/mobilnisite/slovnik/res/)) a šifrovacího/integritního klíče (CK/IK). RES je odeslána zpět do sítě pro ověření, zatímco CK/IK jsou použity UE a sítí k odvození relačních klíčů, které šifrují a chrání integritu všech následných rádiových komunikací. Tento proces, známý jako AKA, zajišťuje vzájemnou autentizaci a vytváří zabezpečený kanál.

Klíčové komponenty uvnitř WIM zahrnují souborový systém (MF, DF, EF), který ukládá IMSI, apleťy řízené operátorem a síťově specifické soubory; kryptografický procesor pro provádění algoritmů; a zabezpečený operační systém, který izoluje aplikace. Jeho role je zásadní pro síťovou bezpečnost a správu účastníků. Odděluje identitu účastníka od hardwaru zařízení, což umožňuje uživatelům měnit zařízení přesunutím WIM (pokud je výměnný) a umožňuje operátorům vzdáleně poskytovat přihlašovací údaje (prostřednictvím SM-DP+ pro eSIM). WIM je kořenem důvěry pro celé mobilní spojení, čímž zabraňuje zneužití identity a odposlechu. Také hostí další služby operátora, jako je SIM Toolkit pro nadstandardní služby.

## K čemu slouží

WIM byl vytvořen k řešení základních problémů mobility účastníků, bezpečnosti a přenositelnosti služeb v celulárních sítích. V raných analogových systémech byla identita účastníka vázána na zařízení, což bylo nebezpečné a nepružné. Zavedení fyzické SIM karty (typu WIM) s GSM oddělilo uživatelský účet od telefonu, což umožnilo uživatelům snadno měnit telefony a operátorům bezpečně distribuovat autentizační údaje. Primární problém, který řešil, byla bezpečná a škálovatelná autentizace pro miliony uživatelů.

Vývoj od SIM k USIM a k vnořeným WIM byl motivován pokračujícími výzvami. Fyzické SIM karty zabírají místo, jsou náchylné k poškození a jsou nepraktické pro IoT zařízení. Koncept WIM, formalizovaný v 3GPP, zobecňuje zabezpečený modul pro řešení těchto omezení. eSIM (vnořený WIM) řeší problém vzdáleného poskytování, což umožňuje, aby byla zařízení vyrobena v továrně a později připojena k libovolnému operátoru přes vzduch, což je klíčové pro automobilový průmysl, nositelnou elektroniku a trh IoT. iSIM (integrovaný WIM) dále řeší omezení prostoru a nákladů integrací zabezpečeného prvku do hlavního čipového systému zařízení. Každý vývoj zachovává základní účel: poskytování standardizovaného, bezpečného a přenosného kotvení pro identitu účastníka a síťovou autentizaci v stále rozmanitějším ekosystému zařízení.

## Klíčové vlastnosti

- Bezpečné uložení dlouhodobé identity účastníka (IMSI) a tajného autentizačního klíče (K)
- Provádění algoritmů pro autentizaci a dohodu klíčů (AKA) (Milenage, TUAK)
- Hostování síťových aplikací (SIM, USIM, ISIM) pro přístup k 2G, 3G, 4G, 5G a IMS
- Odolný hardwarový design proti neoprávněné manipulaci, který zabraňuje extrakci a klonování klíčů
- Standardizované rozhraní (UICC, eUICC) pro komunikaci s modemem zařízení
- Podpora vzdáleného poskytování a správy profilů operátora (pro eSIM)

## Související pojmy

- [SIM – Subscriber Identity Module / Universal Subscriber Identity Module](/mobilnisite/slovnik/sim/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [ISIM – IMS Subscriber Identity Module](/mobilnisite/slovnik/isim/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification

---

📖 **Anglický originál a plná specifikace:** [WIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/wim/)
