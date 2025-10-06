---
author: Patrick Zandl
categories:
- AI
- Claude
- Anthropic
- Claude Code
layout: post
post_excerpt: Praktický návod na využití kontrolních bodů v Claude Code 2.0 pro bezpečné experimentování s kódem a efektivní správu změn během vývoje.
summary_points:
- Kontrolní body vytvářejte před každou rizikovou změnou nebo experimentem
- Používejte popisné názvy kontrolních bodů pro snadnou orientaci
- Kombinujte automatické a manuální kontrolní body podle typu úkolu
- Kontrolní body jsou určeny pro experimentování, ne pro trvalou správu verzí
- Menu obnovení nabízí flexibilní možnosti vrácení změn
- Pravidelně mažte staré kontrolní body po dokončení experimentů
title: Jak efektivně používat kontrolní body v Claude Code 2.0
---

Kontrolní body v Claude Code 2.0 představují mechanismus pro rychlé ukládání a obnovení stavu projektu během vývoje. Jsou novinkou ve V2 a já si na ně zvykám. Podělím se s vámi o dosavadní poznatky a moje workflow, jak body obnovy v CC používám. 

## Základní ovládání kontrolních bodů

Spuštění Claude Code v adresáři projektu provedete příkazem `claude`, jak obvyklé. Systém automaticky vytváří kontrolní body před každou úpravou souborů prostřednictvím nástrojů pro editaci. Pro manuální vytvoření kontrolního bodu použijte příkaz:

```
checkpoint create "popis stavu"
```

Přístup k menu obnovení získáte dvojím stisknutím klávesy Esc nebo zadáním příkazu `/rewind`. Menu zobrazí všechny dostupné kontrolní body s časovými značkami a popisy.

## Kdy vytvářet kontrolní body

Vytváření kontrolních bodů má smysl v těchto situacích:

**Před rizikovými refaktoringy.** Když chcete přestrukturovat kód, změnit architekturu nebo provést rozsáhlé úpravy napříč více soubory, vytvořte kontrolní bod. Pokud refaktoring způsobí problémy, můžete se okamžitě vrátit k funkčnímu stavu.

**Na konci úspěšné implementace funkce.** Když něco funguje a testy procházejí, uložte tento stabilní bod. Slouží jako základ pro další vývoj. Použijte popisný název jako `checkpoint user-authentication-working` nebo `checkpoint api-integration-complete`.

**Před experimentálními změnami.** Chcete vyzkoušet jiný přístup nebo algoritmus, ale nejste si jisti výsledkem? Vytvořte kontrolní bod a experimentujte bez obav. Pokud experiment selže, obnovíte předchozí stav a zkusíte jiný přístup.

**Při práci na kritických částech systému.** Bezpečnostní kód, databázové operace nebo platební integrace vyžadují zvláštní pozornost. Kontrolní body umožňují bezpečně testovat různé implementace, protože CC má občas tendenci to rozhasit. 

**Po dokončení dílčího úkolu v rámci větší funkce.** Komplexní funkce rozvíjejte postupně s kontrolními body mezi kroky. Pokud pozdější krok způsobí problémy, neztratíte práci na předchozích částech.

## Pojmenování kontrolních bodů

Používejte popisné názvy, které jasně identifikují stav projektu:

- `basic-server-setup` - holý funkční server
- `database-connection-working` - připojení k databázi funguje
- `user-registration-complete` - registrace uživatelů dokončena
- `before-jwt-refactor` - před přechodem na JWT autentizaci
- `api-endpoints-tested` - všechny koncové body otestovány

Vyhýbejte se obecným názvům jako `checkpoint1`, `test` nebo `working`, které neposkytují informaci o obsahu, protože když to budete potřebovat obnovit, tak si fakt nevybavíte, co jste tím mysleli...

## Režimy obnovení

Menu obnovení nabízí tři možnosti podle typu změn, které chcete vrátit:

**Pouze konverzace** vrací konverzaci k předchozí zprávě, ale zachovává všechny změny kódu. Používejte, když chcete změnit směr diskuse s Claude Code, ale vytvořený kód je v pořádku.

**Pouze kód** vrací změny souborů do předchozího stavu, ale ponechává historii konverzace. Vhodné, když Claude Code provedl špatné úpravy souborů, ale chcete pokračovat ve stejném kontextu diskuse.

**Kód i konverzace** obnovuje kompletní stav projektu včetně diskuse. Používejte pro úplný návrat k předchozímu bodu při zásadních problémech.

## Pracovní cyklus s kontrolními body

Efektivní využití kontrolních bodů následuje tento vzorec:

1. **Vytvoření kontrolního bodu** ve stabilním stavu, kdy vše funguje
2. **Volné experimentování** - požádejte Claude Code o změny, zkuste různé přístupy
3. **Vyhodnocení výsledků** - otestujte, zda změny fungují podle očekávání
4. **Rozhodnutí** - buď zachováte změny a vytvoříte nový kontrolní bod, nebo obnovíte předchozí stav a zkusíte jiný přístup
5. **Opakování cyklu** pro další část vývoje

Tento vzorec umožňuje odvážné experimentování bez rizika ztráty funkčního kódu.

## Omezení kontrolních bodů

Kontrolní body sledují pouze soubory upravené během aktuální relace prostřednictvím nástrojů Claude Code pro editaci souborů. Systém nezachycuje:

- Změny provedené bash příkazy (`rm`, `mv`, `cp`, `mkdir` atd.)
- Manuální úpravy souborů mimo Claude Code
- Změny z jiných souběžných relací (pokud nemodifikují stejné soubory)

Pokud kombinujete ruční úpravy s Claude Code, uvědomte si, že kontrolní body neobsahují ruční změny. Pro komplexní správu verzí včetně všech typů změn používejte Git.

## Kontrolní body versus Git

Kontrolní body nejsou náhradou systému Git, ale doplňkem pro jiný účel:

**Kontrolní body** slouží k rychlému experimentování během aktivního vývoje. Vytváříte je často, používáte liberálně a mažete po dokončení experimentů. Jsou lokální pro relaci Claude Code a neukládají se do repozitáře.

**Git závazky** představují trvalé milníky ve vývoji projektu. Vytváříte je méně často, po dokončení funkčních celků, s pečlivě napsanými komentáři. Sdílíte je s týmem a uchovávají se v historii projektu.

Typický pracovní postup kombinuje obojí: experimentujte s Claude Code a kontrolními body, dokud nedosáhnete funkčního řešení, pak vytvořte Git závazek pro trvalé uložení.

## Údržba kontrolních bodů

Kontrolní body zabírají místo a při velké relaci se menu obnovení stává nepřehledným. Pravidelně promazávejte staré kontrolní body, které už nepotřebujete. Ponechejte pouze:

- Poslední stabilní stav
- Kontrolní body před významnými rozhodovacími body
- Body, ke kterým se možná budete chtít vrátit

Po dokončení funkce a vytvoření Git závazku můžete obvykle smazat všechny kontrolní body z dané relace.

## Praktický příklad použití

Při vývoji autentizačního systému pro REST API postupujete takto:

Vytvoříte základní Express.js server s jednoduchým koncovým bodem. Otestujete funkčnost a vytvoříte kontrolní bod `checkpoint basic-server-working`.

Požádáte Claude Code o přidání registrace uživatelů s bcrypt hashováním hesel. Po implementaci otestujete registrační koncový bod. Pokud funguje, vytvoříte `checkpoint registration-working`. Pokud ne, obnovíte `basic-server-working` a zkusíte jiný přístup.

Přidáváte JWT autentizaci. Implementace je složitější a může selhat. Před začátkem máte kontrolní bod `registration-working`. Požádáte Claude Code o implementaci JWT. Objeví se chyba - chybí JWT_SECRET v souboru .env. Místo pokusu o opravu, která může vést ke složitějším problémům, obnovíte `registration-working`, opravíte konfiguraci a požádáte Claude Code o implementaci znovu.

Když JWT autentizace funguje, vytvoříte `checkpoint jwt-auth-working`. Nyní můžete experimentovat s obnovovacími tokeny nebo jinými funkcemi s jistotou, že máte funkční základ.

## Práce s kontrolními body při vývoji funkcí

Při implementaci komplexní funkce rozdělte práci na menší kroky a vytvořte kontrolní bod po každém kroku:

1. Základní struktura - kontrolní bod
2. Integrace s databází - kontrolní bod
3. Validace vstupů - kontrolní bod
4. Zpracování chyb - kontrolní bod
5. Testy - kontrolní bod

Pokud kterýkoli krok způsobí problémy v předchozích částech, vrátíte se o krok zpět místo pokusu opravit kaskádu chyb.

## Shrnutí nejlepší praxe

Vytvářejte kontrolní bod vždy, když máte funkční kód a chystáte se k riskantní změně. Používejte popisné názvy zachycující stav projektu. Testujte změny před vytvořením nového kontrolního bodu. Neváhejte obnovit předchozí stav při problémech - to je účel kontrolních bodů. Kombinujte kontrolní body pro experimentování s Git pro trvalou správu verzí. Pravidelně mažte nepotřebné kontrolní body pro přehlednost.

Kontrolní body v [Claude Code](https://docs.claude.com/en/docs/claude-code) mění programování s asistencí umělé inteligence z opatrného postupu na odvážné experimentování. Systém záchytných bodů umožňuje zkoušet různé přístupy bez obav ze ztráty funkčního kódu, což vede k rychlejšímu nalezení optimálního řešení.