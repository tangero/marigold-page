---
slug: "scvl"
url: "/mobilnisite/slovnik/scvl/"
type: "slovnik"
title: "SCVL – Speech Coder Version List"
date: 2025-01-01
abbr: "SCVL"
fullName: "Speech Coder Version List"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/scvl/"
summary: "SCVL je seznam identifikující podporované verze řečových kodeků mobilní stanice (MS). Používá se při sestavování hovoru k vyjednání nejvyššího vzájemně podporovaného řečového kodeku mezi MS a sítí. Tí"
---

SCVL je seznam identifikující verze řečových kodeků, které mobilní stanice podporuje. Používá se při sestavování hovoru k vyjednání nejvyššího vzájemně podporovaného kodeku se sítí za účelem optimální kvality hlasu a interoperability.

## Popis

Speech Coder Version List (SCVL) je parametr definovaný ve specifikaci 3GPP TS 43.903, používaný primárně v GSM a příbuzných systémech. Jedná se o datovou strukturu uloženou v mobilní stanici ([MS](/mobilnisite/slovnik/ms/)), která vyjmenovává verze řečových kodeků, které terminál podporuje. Při sestavování hovoru iniciovaného mobilní stanicí nebo jí přijímaného zařadí MS svůj SCVL do signalizačních zpráv, například do [CC](/mobilnisite/slovnik/cc/) (Call Control) SETUP nebo do procedur přiřazení kanálu. Síť, typicky Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) nebo Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)), tento seznam přijme a porovná jej s vlastními podporovanými verzemi kodeků a možnostmi volané strany (pokud jsou známé). Na základě tohoto vyjednávání síť vybere řečový kodek s nejvyšší prioritou, který je společný všem zúčastněným stranám hovoru. Tento zvolený kodek určuje algoritmy pro kódování a dekódování řeči použité pro hlasový provoz, což ovlivňuje kvalitu hlasu, využití šířky pásma a odolnost vůči chybám.

Z architektonického hlediska SCVL funguje v rámci vrstvy řízení hovoru v MS a v síti. Je součástí informací o možnostech terminálu, které si mezi sebou MS a síť vyměňují. Seznam je strukturován jako uspořádaná množina identifikátorů kodeků, často odrážející preferenční nebo kapacitní pořadí. Mezi běžné řečové kodeky v kontextu GSM patří Full Rate ([FR](/mobilnisite/slovnik/fr/)), Half Rate ([HR](/mobilnisite/slovnik/hr/)), Enhanced Full Rate ([EFR](/mobilnisite/slovnik/efr/)) a Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) kodeky, každý s různými verzemi. SCVL umožňuje MS indikovat podporu více kodeků, což síti umožňuje učinit informovaný výběr na základě faktorů, jako je zatížení sítě (např. volba HR při přetížení k úspoře kapacity) nebo optimalizace kvality (např. volba EFR nebo AMR pro lepší kvalitu).

Role SCVL je klíčová pro zpětnou i dopřednou kompatibilitu. Jak se sítě vyvíjejí, jsou zaváděny nové řečové kodeky pro zlepšení kvality nebo efektivity. Starší MS nemusí podporovat novější kodeky a naopak. SCVL usnadňuje interoperabilitu tím, že umožňuje síti v případě potřeby přepnout na starší, společně podporovaný kodek. Proces vyjednávání je pro uživatele typicky transparentní, ale přímo ovlivňuje vnímanou kvalitu hlasu. Během provozu, po výběru kodeku, síť nakonfiguruje příslušný provozní kanál a informuje o tom MS prostřednictvím příkazů pro přiřazení. MS následně přepne své funkce zpracování řeči na dohodnutý kodek. SCVL je klíčovým prvkem pro vícekódové kodeky, jako je AMR, kde seznam může indikovat podporu více přenosových rychlostí a režimů kodeku, což umožňuje dynamickou adaptaci během hovoru na základě rádiových podmínek.

## K čemu slouží

SCVL byl vytvořen k řešení problému interoperability řečových kodeků v heterogenních mobilních sítích. V počátcích GSM byl používán jediný řečový kodek (Full Rate). Nicméně se zavedením vylepšených kodeků, jako je Half Rate (pro kapacitu) a Enhanced Full Rate (pro kvalitu), začaly sítě a koncová zařízení podporovat více typů kodeků. Bez standardizovaného vyjednávacího mechanismu by hovory mohly selhávat nebo by se používal suboptimální kodek, což by vedlo ke špatné kvalitě hlasu nebo neefektivnímu využití spektra. SCVL poskytl strukturovaný způsob, jak může mobilní stanice prezentovat své možnosti kodeků, což síti umožňuje vybrat nejlepší vzájemně podporovanou variantu. Tím bylo zajištěno, že hovory lze vždy sestavit s nejvyšší možnou kvalitou vzhledem k omezením obou stran.

Historická motivace vychází z potřeby optimalizovat síťové zdroje při zachování kvality služeb. Kodeky Half Rate umožnily operátorům zdvojnásobit hlasovou kapacitu použitím menší šířky pásma na hovor, ale vyžadovaly kompatibilní koncová zařízení. Enhanced Full Rate nabízel lepší kvalitu hlasu, ale nebyl všeobecně podporován. SCVL umožnil plynulé snížení i zvýšení kvality: při přetížení mohla síť upřednostnit mobilní stanice podporující HR, aby uvolnila zdroje, zatímco za dobrých podmínek mohla vybrat EFR nebo AMR pro vyšší kvalitu. Tato flexibilita byla klíčová pro operátory spravující omezené rádiové spektrum a různorodou základnu účastníků.

SCVL dále podpořil zavedení adaptivních kodeků, jako je AMR, které dynamicky upravují přenosovou rychlost na základě podmínek rádiového kanálu. Seznam mohl indikovat podporu více režimů AMR, což síti umožňovalo během hovoru nařizovat změny režimu. Tím se zlepšila robustnost hlasové služby v proměnlivých signálových podmínkách. Standardizací této výměny informací o možnostech 3GPP zajistilo, že koncová zařízení a síťové prvky od různých dodavatelů mohou bezproblémově spolupracovat, což podpořilo konkurenci a inovace v mobilním ekosystému při současné ochraně investic do stávající infrastruktury.

## Klíčové vlastnosti

- Kóduje podporované verze řečových kodeků mobilní stanice
- Používá se v signalizaci při sestavování hovoru pro vyjednání kodeku
- Umožňuje výběr nejvyššího vzájemně podporovaného kodeku
- Podporuje zpětnou kompatibilitu se staršími kodeky
- Umožňuje síti řízený výběr kodeku na základě zatížení nebo kvality
- Klíčový pro provoz adaptivního vícekódového kodeku (AMR)

## Definující specifikace

- **TR 43.903** (Rel-19) — Feasibility Study for A-interface over IP

---

📖 **Anglický originál a plná specifikace:** [SCVL na 3GPP Explorer](https://3gpp-explorer.com/glossary/scvl/)
