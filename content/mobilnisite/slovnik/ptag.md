---
slug: "ptag"
url: "/mobilnisite/slovnik/ptag/"
type: "slovnik"
title: "PTAG – Primary Timing Advance Group"
date: 2025-01-01
abbr: "PTAG"
fullName: "Primary Timing Advance Group"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ptag/"
summary: "Logické seskupení obslužných buněk pro UE v agregaci nosných, které sdílí společnou hodnotu časového předstihu pro synchronizaci vysílání v uplinku. Je klíčové pro efektivní správu časování uplinku na"
---

PTAG je Primární skupina časového předstihu (Primary Timing Advance Group), logické seskupení obslužných buněk v agregaci nosných, které sdílí společnou hodnotu časového předstihu (Timing Advance) pro synchronizaci vysílání v uplinku.

## Popis

Primární skupina časového předstihu (PTAG) je koncept definovaný ve specifikacích 3GPP pro sítě LTE-Advanced a 5G NR využívající agregaci nosných ([CA](/mobilnisite/slovnik/ca/)). Při agregaci nosných může být uživatelské zařízení (UE) nakonfigurováno s více komponentními nosnými ([CC](/mobilnisite/slovnik/cc/)) pro zvýšení celkové šířky pásma a datového propustnosti. Základním požadavkem pro vysílání v uplinku je, aby signály z UE dorazily na základnovou stanici (eNodeB v LTE, gNodeB v NR) v rámci cyklického prefixu, a tak se předešlo mezi-symbolovému rušení. To je řízeno příkazem časového předstihu ([TA](/mobilnisite/slovnik/ta/)), který nařídí UE, aby posunulo časování svého vysílání na základě vzdálenosti od buňky.

Z architektonického hlediska, když je UE nakonfigurováno s více obslužnými buňkami (Primární buňkou, PCell, a jednou či více Sekundárními buňkami, SCell), jsou tyto buňky organizovány do Skupin časového předstihu (TAG). PTAG je konkrétní TAG, který obsahuje PCell. Všechny obslužné buňky ve stejném TAG sdílejí identickou hodnotu TA. To proto, že buňky ve stejném TAG jsou typicky umístěny na stejném místě základnové stanice nebo jsou geograficky dostatečně blízko, takže rozdíl v zpoždění šíření je zanedbatelný vzhledem k délce cyklického prefixu. UE udržuje pro každý TAG samostatný TA časovač a příkaz TA přijatý pro buňku v rámci TAG aplikuje na všechny buňky v této skupině.

Jak to funguje, je založeno na procedurách náhodného přístupu ([RACH](/mobilnisite/slovnik/rach/)) a řídicích prvcích [MAC](/mobilnisite/slovnik/mac/) (MAC [CE](/mobilnisite/slovnik/ce/)). Počáteční TA pro PTAG je stanovena, když UE provede proceduru náhodného přístupu na PCell. Následné aktualizace TA pro PTAG mohou být přijaty prostřednictvím příkazů TA v MAC CE, které jsou identifikovány ID TAG. UE aplikuje toto nařízené nastavení na hodnotu TA pro všechny buňky v PTAG. Síť (eNodeB/gNodeB) spravuje seskupování a rozhoduje, které SCell patří do PTAG (tj. jsou umístěny společně s PCell) a které mohou patřit do Sekundárních TAG (sTAG), pokud jsou obsluhovány z jiné vzdálené rádiové jednotky nebo lokality. Konfigurace TAG je signalizována UE prostřednictvím zpráv [RRC](/mobilnisite/slovnik/rrc/) pro překonfigurování spojení.

Její role je klíčová pro efektivní správu synchronizace uplinku v nasazeních s více nosnými. Seskupením buněk síť snižuje signalizační režii – místo odesílání jednotlivých příkazů TA pro každou buňku jeden příkaz aktualizuje celou skupinu. Také zjednodušuje implementaci UE, protože UE potřebuje spravovat pouze několik TA časovačů namísto jednoho na buňku. Toto seskupení je základním kamenem pro funkce jako duální konektivita a přenos z více [TRP](/mobilnisite/slovnik/trp/), kde buňky z různých fyzických lokalit vyžadují samostatné TAG, aby bylo zohledněno rozdílné zpoždění šíření.

## K čemu slouží

PTAG byl zaveden, aby vyřešil problém synchronizace časování uplinku ve scénářích agregace nosných. Před agregací nosných bylo UE připojeno k jedné buňce a stačila jediná hodnota TA. Se zavedením CA v LTE-Advanced (Rel-10) mohlo UE přijímat a vysílat na více komponentních nosných, potenciálně ze stejné nebo různých lokalit základnových stanic. Pokud by všechny buňky používaly stejnou TA, signály ze vzdálené SCell by mohly dorazit na její přijímač nesynchronizované, což by způsobilo rušení. Naivní řešení nezávislé TA pro každou buňku by vytvořilo nadměrnou signalizační režii a složitost UE.

Koncept Skupin časového předstihu, s PTAG jako skupinou obsahující kotvovou PCell, poskytl elegantní řešení. Uznal, že v mnoha nasazeních, zejména u agregace nosných na jednom místě, jsou SCell umístěny společně s PCell, a tedy zažívají stejné zpoždění šíření. Jejich seskupení umožňuje spravovat je všechny jednou hodnotou TA. Pro SCell na vzdálených rádiových jednotkách (tvořících sTAG) je udržována samostatná TA. Tím byly odstraněny limity přístupu jedné TA pro všechny, a zároveň se předešlo režii TA na buňku. Jeho vytvoření bylo motivováno potřebou učinit agregaci nosných praktickou a efektivní, což umožnilo škálování šířky pásma definující výkon 4G a 5G bez zatížení řídicího kanálu nebo zpracování v UE.

## Klíčové vlastnosti

- Obsahuje Primární buňku (PCell) UE v agregaci nosných
- Všechny obslužné buňky v rámci PTAG sdílejí společnou hodnotu časového předstihu
- Počáteční TA je stanovena procedurou náhodného přístupu na PCell
- Aktualizace TA jsou aplikovány prostřednictvím řídicích prvků MAC identifikovaných ID TAG
- Snižuje signalizační režii ve srovnání se správou TA na úrovni jednotlivých buněk
- Klíčová pro správu zarovnání uplinku v nasazeních s více nosnými a více TRP

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PTAG na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptag/)
