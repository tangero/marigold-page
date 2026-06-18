---
slug: "watp"
url: "/mobilnisite/slovnik/watp/"
type: "slovnik"
title: "WATP – Wayside Automatic Train Protection"
date: 2026-01-01
abbr: "WATP"
fullName: "Wayside Automatic Train Protection"
category: "IoT"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/watp/"
summary: "Funkce systému 3GPP pro železniční komunikaci, která umožňuje funkčnost automatické ochrany vlaku (ATP) pomocí zařízení podél trati připojených přes síť 3GPP, namísto tradičních systémů založených na"
---

WATP je funkce železničního systému podle 3GPP, která využívá zařízení podél trati (wayside equipment) a konektivitu mobilní sítě k přenosu životně důležitých bezpečnostních povelů z centrálního řídicího systému na vlaky pro automatickou ochranu vlaku.

## Popis

Wayside Automatic Train Protection (WATP) je standardizovaná architektura v rámci 3GPP, která podporuje bezpečnostně kritické řídicí systémy železnic využitím mobilní síťové technologie 3GPP pro komunikaci mezi vlaky a infrastrukturou podél trati. Automatická ochrana vlaku je základní bezpečnostní systém, který nepřetržitě monitoruje rychlost a polohu vlaku a vynucuje bezpečná povolení k jízdě, aby zabránil kolizím, vykolejením v důsledku nadměrné rychlosti a vjezdům do obsazených úseků trati. Tradiční [ATP](/mobilnisite/slovnik/atp/) spoléhá na balízy (majáky) na trati nebo na souvislé kolejové obvody, jejichž instalace a údržba jsou nákladné.

Architektura WATP zavádí bezdrátový, na síti založený přístup. Mezi klíčové komponenty patří palubní jednotka (OBU) ve vlaku, která obsahuje životně důležitou ATP logiku; wayside ATP jednotka (WAU), což je zařízení podél trati, které určuje povolení k jízdě na základě obsazenosti trati a stavu závislostí; a síť 3GPP (4G LTE nebo 5G NR), která poskytuje přenosový prostředek mezi nimi. WAU se k mobilní síti připojuje jako uživatelské zařízení (UE) nebo přes pevné síťové připojení k vyhrazenému serveru. Používá služby definované 3GPP, potenciálně vylepšené pro ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)), k přenosu zpráv s povolením k jízdě ([MA](/mobilnisite/slovnik/ma/)) do OBU cílového vlaku.

Jak to funguje: jde o nepřetržitý cyklus stanovení a přenosu. Wayside ATP jednotka vypočítá bezpečný pohybový profil (včetně cílové rychlosti a brzdné křivky) pro vlak na základě hlášené polohy vlaku (přes [GNSS](/mobilnisite/slovnik/gnss/) nebo jiné senzory), stavu návěstidel a výhybek ze závislostí a známých poloh ostatních vlaků. Tato životně důležitá zpráva MA je pak paketizována a odeslána přes síť 3GPP konkrétnímu vlaku, adresována pomocí jeho síťové identity (např. IP adresy). OBU vlaku tuto zprávu přijme, ověří její integritu a autenticitu pomocí bezpečnostních mechanismů a poté porovná autorizované MA se skutečnou rychlostí a polohou vlaku. Pokud je zjištěno porušení (např. překročení rychlosti), OBU automaticky zahájí brzdění, aby uvedlo vlak do bezpečného stavu. Systém vyžaduje extrémně vysokou úroveň spolehlivosti, dostupnosti a nízkou latenci, což je řešeno funkcemi 5G NR, jako je URLLC, síťové segmentování a komunikace zařízení-zařízení pro přímá upozornění mezi vlaky.

## K čemu slouží

WATP byl vytvořen za účelem modernizace a snížení nákladů železničních zabezpečovacích a bezpečnostních systémů využitím komerční mobilní síťové technologie. Tradiční systémy ochrany vlaku, jako jsou kolejové obvody, počítače náprav a balízy podél trati, vyžadují rozsáhlou fyzickou infrastrukturu instalovanou podél celého železničního koridoru. To vede k velmi vysokým kapitálovým výdajům ([CAPEX](/mobilnisite/slovnik/capex/)) pro nové tratě a významným provozním výdajům ([OPEX](/mobilnisite/slovnik/opex/)) na údržbu, zejména v náročném prostředí nebo na dlouhých, odlehlých vzdálenostech.

Primární problém, který WATP řeší, je poskytnutí flexibilní, škálovatelné a nákladově efektivní alternativy pro [ATP](/mobilnisite/slovnik/atp/), zejména pro regionální tratě nebo tratě s nízkou hustotou provozu, kde je instalace tradičních systémů ekonomicky neúnosná. Řeší také potřebu nepřetržité výměny dat s vysokou kapacitou pro budoucí železniční provoz, jako je video v reálném čase pro detekci překážek nebo monitorování stavu, což starší systémy nepodporují. Motivací pro jeho standardizaci v 3GPP Rel-16 bylo uznání železnic jako klíčového vertikálního odvětví pro 5G, se specifickými požadavky na komunikaci pro mise kritické z hlediska bezpečnosti, které by mohly být splněny vylepšením stávajících standardů 3GPP spíše než vývojem zcela samostatných proprietárních bezdrátových řešení.

Řeší omezení předchozích bezdrátových řešení pro železnice, která byla často izolovanými, proprietárními sítěmi (jako [GSM-R](/mobilnisite/slovnik/gsm-r/)), nabízejícími omezenou šířku pásma a zastaralou technologickou základnu. WATP, postavený na 4G/5G, poskytuje migrační cestu k budoucně odolnému, na IP založenému platformě, která může podporovat jak bezpečnostně kritické ATP, tak i další provozní/pasažérské služby na sdílené infrastruktuře, umožněné síťovým segmentováním pro zajištění izolace a garancí výkonu pro bezpečnostní segment.

## Klíčové vlastnosti

- Využívá mobilní sítě 3GPP (LTE, 5G NR) pro bezpečnostně kritickou řídicí komunikaci v železniční dopravě
- Definuje architekturu pro Wayside ATP jednotky a palubní jednotky komunikující přes rozhraní Uu sítě 3GPP
- Podporuje přenos životně důležitých zpráv s povolením k jízdě (MA) z místa podél trati na vlak
- Vyžaduje charakteristiky ultra-spolehlivé komunikace s nízkou latencí (URLLC), jak jsou definovány pro 5G
- Umožňuje potenciální snížení nákladů ve srovnání s pevnou signalizační infrastrukturou podél trati
- Usnadňuje integraci s dalšími službami FRMCS (Future Railway Mobile Communication System)

## Související pojmy

- [FRMCS – Future Railway Mobile Communication System](/mobilnisite/slovnik/frmcs/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TR 22.889** (Rel-17) — FRMCS Study; Stage 1
- **TR 22.989** (Rel-20) — FRMCS Analysis and Requirements

---

📖 **Anglický originál a plná specifikace:** [WATP na 3GPP Explorer](https://3gpp-explorer.com/glossary/watp/)
