---
slug: "anqp"
url: "/mobilnisite/slovnik/anqp/"
type: "slovnik"
title: "ANQP – Access Network Query Protocol"
date: 2025-01-01
abbr: "ANQP"
fullName: "Access Network Query Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/anqp/"
summary: "ANQP je dotazovací/odpovědací protokol používaný mobilními zařízeními k získání informací o dostupných přístupových sítích před připojením. Umožňuje efektivní výběr sítě tím, že poskytuje metadata o s"
---

ANQP je dotazovací/odpovědací protokol používaný mobilními zařízeními k zjištění schopností a politik přístupové sítě před připojením, což umožňuje efektivní výběr sítě a převádění provozu na Wi-Fi (Wi-Fi offloading) v prostředí propojení 3GPP a WLAN.

## Popis

Access Network Query Protocol (ANQP) je dotazovací/odpovědací protokol definovaný specifikacemi Hotspot 2.0 (HS2.0) Wi-Fi Alliance a přijatý konsorciem 3GPP pro propojení s WLAN přístupovými sítěmi. ANQP funguje na aplikační vrstvě a jako transportní mechanismus využívá rámce služby Generic Advertisement Service (GAS) přes sítě [IEEE](/mobilnisite/slovnik/ieee/) 802.11. Protokol umožňuje mobilním zařízením (User Equipment, UE) dotazovat se přístupových sítí na informace bez nutnosti navázání plného síťového připojení, což umožňuje informovaná rozhodnutí o výběru sítě na základě dostupných služeb, schopností a politik.

ANQP pracuje v modelu klient-server, kde UE funguje jako ANQP klient a přístupový bod (Access Point, [AP](/mobilnisite/slovnik/ap/)) nebo Access Network Query Server (ANQS) funguje jako ANQP server. UE odesílá ANQP dotazovací rámce obsahující identifikátory specifických informačních elementů, aby požádalo o konkrétní typy síťových informací. ANQP server odpovídá odpovídajícími ANQP odpovědními rámci obsahujícími požadované informační elementy. Tato výměna probíhá během fáze před přidružením (pre-association phase), což umožňuje UE vyhodnotit více sítí předtím, než se k jedné z nich přidruží.

Klíčovými komponentami ANQP jsou implementace ANQP klienta v UE, ANQP server (který může být integrován v AP nebo samostatné síťové entitě) a ANQP informační elementy definující strukturu dotazů a odpovědí. Protokol podporuje různé informační elementy včetně typu síťového ověření, seznamu konsorcií pro roaming (roaming consortium), informací o místě (venue), domény [NAI](/mobilnisite/slovnik/nai/) (Network Access Identifier) realm, informací o síti 3GPP, seznamu názvů domén a dostupnosti typu IP adresy. Tyto elementy poskytují komplexní metadata o schopnostech a službách přístupové sítě.

V architekturách 3GPP hraje ANQP klíčovou roli v řešeních pro propojení s WLAN založených na [ANDSF](/mobilnisite/slovnik/andsf/) (Access Network Discovery and Selection Function) a ePDG (evolved Packet Data Gateway). Protokol umožňuje UE objevovat WLAN sítě založené na přihlašovacích údajích 3GPP a získávat potřebné informace pro bezproblémové ověření a připojení. ANQP dotazy mohou obsahovat specifické 3GPP informační elementy, které pomáhají UE identifikovat sítě podporující ověřování EAP-AKA/EAP-AKA', porozumět dostupným informacím o PLMN (Public Land Mobile Network) a určit politiky výběru sítě.

Návrh protokolu klade důraz na efektivitu a bezpečnost. Výměny ANQP probíhají přes chráněné rámce pro správu (protected management frames), pokud je to možné, ačkoli základní ANQP dotazy mohou být během počátečního objevování odesílány nešifrované. Protokol zahrnuje mechanismy pro fragmentaci a opětovné sestavení velkých informačních elementů prostřednictvím více GAS rámců. ANQP také podporuje dodavatelsky specifické (vendor-specific) informační elementy, což umožňuje rozšiřitelnost a přizpůsobení ze strany síťových operátorů a výrobců zařízení.

## K čemu slouží

ANQP byl vytvořen, aby odstranil omezení tradičních mechanismů objevování Wi-Fi sítí, které se spoléhaly primárně na vysílání SSID a manuální konfiguraci. Před ANQP měla mobilní zařízení před připojením omezený přehled o schopnostech sítě, což často vyžadovalo, aby uživatelé ručně vybírali sítě a zadávali přihlašovací údaje, aniž by věděli, zda síť podporuje požadované služby nebo bezpečnostní protokoly. Tento přístup byl neefektivní pro bezproblémovou mobilitu a vedl ke špatným uživatelským zkušenostem, zejména v roamingových scénářích.

Protokol konkrétně řeší problém informovaného výběru sítě v heterogenních sítích, zejména pro propojení 3GPP a WLAN. Když mobilní operátoři začali integrovat Wi-Fi do svých síťových architektur pro převádění provozu (traffic offloading) a zvýšení kapacity, potřebovali standardizovaný způsob, jak zařízením umožnit automatické objevování a výběr vhodných WLAN přístupových bodů na základě politik operátora, dostupných služeb a metod ověřování. ANQP tuto schopnost poskytuje tím, že umožňuje zařízením dotazovat se sítí na podrobné informace před navázáním připojení.

Historický kontext ukazuje, že ANQP vznikl spolu s iniciativou Hotspot 2.0 Wi-Fi Alliance, která si kladla za cíl vytvořit Wi-Fi sítě na úrovni operátorů (carrier-grade) s bezproblémovou konektivitou podobnou té v celulárních sítích. Konsorcium 3GPP přijalo ANQP, aby usnadnilo standardizované propojení mezi celulárními sítěmi a WLAN sítěmi, a řešilo tak rostoucí potřebu inteligentního směrování provozu a výběru sítě ve stále složitějších prostředích heterogenních sítí. Protokol umožňuje naplnění vize 'vždy nejlépe připojen' (always best connected) tím, že poskytuje zařízením informace potřebné k učinění optimálních rozhodnutí o výběru sítě na základě aktuálních podmínek a politik operátora.

## Klíčové vlastnosti

- Objevování sítě před přidružením bez nutnosti plného navázání připojení
- Podpora více informačních elementů včetně typů ověřování a informací o roamingu
- Integrace s metadaty sítě specifickými pro 3GPP pro propojení celulárních a WLAN sítí
- Transport prostřednictvím rámců IEEE 802.11 GAS pro efektivní doručování
- Podpora fragmentace pro velké informační elementy přes více rámců
- Rozšiřitelnost pro specifické potřeby dodavatelů prostřednictvím vlastních informačních elementů

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)

## Definující specifikace

- **TS 23.852** (Rel-12) — Study on GTP-based S2a for WLAN Access
- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 37.834** (Rel-12) — WLAN/3GPP Radio Interworking Study

---

📖 **Anglický originál a plná specifikace:** [ANQP na 3GPP Explorer](https://3gpp-explorer.com/glossary/anqp/)
