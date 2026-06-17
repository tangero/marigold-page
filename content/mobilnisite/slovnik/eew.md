---
slug: "eew"
url: "/mobilnisite/slovnik/eew/"
type: "slovnik"
title: "EEW – Earthquake Early Warning"
date: 2025-01-01
abbr: "EEW"
fullName: "Earthquake Early Warning"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eew/"
summary: "Earthquake Early Warning (EEW) je služba standardizovaná 3GPP, která doručuje rychlá varování na mobilní zařízení po detekci seizmické aktivity. Využívá vysílací (broadcast) schopnosti celulární sítě"
---

EEW je služba standardizovaná 3GPP, která doručuje rychlá varování před zemětřesením na mobilní zařízení prostřednictvím celulárního vysílání (broadcast) s cílem poskytnout kritických několik vteřin varování pro veřejnou bezpečnost.

## Popis

Earthquake Early Warning (EEW) je systém varování veřejnosti standardizovaný 3GPP, navržený k okamžitému doručení varování masovému publiku prostřednictvím mobilních sítí po detekci zemětřesení. Systém je architekturován tak, aby minimalizoval latenci od detekce seizmické události k oznámení veřejnosti. Funguje integrací sítí seizmických senzorů, které detekují primární (P) vlny, s infrastrukturou celulární sítě. Po detekci je vygenerována varovná zpráva a vložena do Cell Broadcast Centre ([CBC](/mobilnisite/slovnik/cbc/)) sítě. CBC následně distribuuje varování prostřednictvím Cell Broadcast Service ([CBS](/mobilnisite/slovnik/cbs/)) přes LTE nebo 5G rádiovou přístupovou síť pomocí System Information Blocks (SIBs) nebo vyhrazených varovných zpráv. Tyto zprávy jsou vysílány na všechna User Equipment (UE) v postižené geografické oblasti, nezávisle na jakémkoli předplatném nebo probíhajícím hovoru, což zajišťuje komplexní pokrytí.

Technická implementace se opírá o existující rámce pro varovné zprávy definované v 3GPP, jako je Public Warning System (PWS), který zahrnuje Earthquake and Tsunami Warning System (ETWS) v LTE a vylepšení Commercial Mobile Alert System ([CMAS](/mobilnisite/slovnik/cmas/)). Zpráva EEW obsahuje kritické informace, jako je odhadovaný čas příchodu destruktivnějších sekundárních (S) vln, odhadovaná intenzita a poloha epicentra. UE po přijetí vysílání zprávu zpracuje a může spustit zvukový alarm, vibrace a varování na obrazovce, i když je zařízení v tichém režimu, čímž je zajištěno upozornění uživatele.

Role EEW v síti spočívá v poskytování služby vysílání (broadcast) s kriticky nízkou latencí a vysokou prioritou. Nevyžaduje žádné nastavení ani potvrzení od UE, což umožňuje okamžité doručení. Síť musí zajistit, aby bylo varování šířeno s minimálním zpožděním přes Core Network do Radio Access Network (RAN) a vysíláno přes správné sledovací oblasti (tracking areas). To zahrnuje koordinaci mezi subjektem generujícím varování (často národní geologickou agenturou), prvky core sítě mobilního operátora (jako je [MME](/mobilnisite/slovnik/mme/) v LTE nebo [AMF](/mobilnisite/slovnik/amf/) v 5GC) a uzly RAN (eNBs/gNBs). Služba je příkladem využití celulárních sítí pro bezpečnost společnosti nad rámec tradiční komunikace.

## K čemu slouží

Účelem služby Earthquake Early Warning je zmírnit dopady zemětřesení tím, že veřejnosti poskytne několik vteřin až desítek vteřin předstižného varování před příchodem nejsilnějšího třesení. Toto krátké okno může být klíčové pro jednotlivce, aby podnikli ochranné kroky, jako je 'padnout na zem, ukrýt se a držet', pro automatizované systémy k zastavení vlaků, uzavření plynových řadů nebo otevření dveří výtahů, a pro záchranné služby k přípravě. Motivací pro její vytvoření v rámci 3GPP je prokázaná účinnost takových systémů v zemích náchylných k zemětřesením, jako je Japonsko a Mexiko, a uznání, že mobilní sítě se svým téměř všudypřítomným pokrytím jsou ideální platformou pro hromadné varování.

Historicky se systémy včasného varování spoléhaly na vyhrazené sirény, rozhlasové nebo televizní vysílání, které měly omezení v dosahu, bezprostřednosti a cílení. Integrace do standardů 3GPP, počínaje Release 8, umožnila standardizovanou, interoperabilní metodu doručování varování přímo na osobní mobilní zařízení. Tím se odstranila omezení předchozích přístupů tím, že bylo umožněno geograficky specifické varování, zajištěno přijetí zprávy i v případě, že uživatel není poblíž tradičního přijímače vysílání, a využito neustálé připravenosti moderních smartphonů. Vytvoření EEW v rámci 3GPP formalizuje protokoly a postupy, což zajišťuje, že různí výrobci síťového zařízení a výrobci zařízení mohou implementovat kompatibilní a spolehlivou službu po celém světě.

## Klíčové vlastnosti

- Hromadné vysílání s nízkou latencí prostřednictvím Cell Broadcast Service (CBS)
- Geografické cílení pro varování pouze postižených oblastí
- Nezávislost na předplatném uživatele nebo stavu zařízení (idle/připojeno)
- Povinná podpora UE pro zpracování a zobrazení varování
- Integrace s externími sítěmi seizmických senzorů
- Využití System Information Blocks (SIBs) pro okamžitou distribuci v RAN

## Související pojmy

- [CBS – Cell Broadcast Service](/mobilnisite/slovnik/cbs/)

## Definující specifikace

- **TR 22.968** (Rel-19) — Study on Public Warning System (PWS)

---

📖 **Anglický originál a plná specifikace:** [EEW na 3GPP Explorer](https://3gpp-explorer.com/glossary/eew/)
