---
author: Patrick Zandl
categories:
- AI
- Claude
- programování
- vzdělávání
- Anthropic
layout: post
post_excerpt: Anthropic představil nový vzdělávací režim pro Claude Code, který učí programátory během psaní kódu a nutí je aktivně přemýšlet o řešeních.
summary_points:
- Claude Code získal nový vzdělávací režim, který aktivně učí programování
- Lite režim vysvětluje osvědčené postupy a kompromisy během kódování
- Learn-by-doing režim pozastavuje práci a vyžaduje od uživatele napsat kritické části
- Funkce využívá TODO(human) značky v kódu pro označení míst k dokončení
- Aktivace probíhá příkazem /output-style s možností vlastních stylů
- Vývoj vedl Drew Bent s týmem z Anthropic AI
title: Claude Code nově učí uživatele programátorských technikám
---

Anthropic rozšířil svůj nástroj Claude Code o vzdělávací funkce, které mění přístup k automatizovanému programování. Nový vzdělávací režim nejen má zvyšit produktivitu, ale aktivně učí uživatele lepším programátorským technikám během samotného procesu tvorby kódu.

## Dva režimy učení

Vzdělávací funkce nabízí dva základní přístupy k učení. _Lite_ režim funguje jako průvodce během kódování - vysvětluje osvědčené postupy, upozorňuje na kompromisy v řešení a zdůvodňuje, proč určité přístupy fungují lépe než jiné. Tento režim nenarušuje pracovní tok a poskytuje kontextové vzdělávání během běžné práce.

Pokročilejší _learn-by-doing_ režim jde výrazně dále. Strategicky pozastavuje automatické generování kódu a vyzývá programátora, aby sám napsal kritické části aplikace. Tyto úseky označuje speciálními značkami TODO(human) přímo v kódu, což vytváří jasné místo pro lidskou intervenci.

## Praktický příklad použití

Při vývoji webové aplikace může Claude Code v learn-by-doing režimu automaticky vygenerovat základní strukturu, ale zastaví se u implementace autentifikace uživatelů. Místo automatického dokončení vloží do kódu značku:

```javascript
// TODO(human): Implementujte ověření JWT tokenu
// Zvažte: bezpečnostní hrozby, expiraci tokenů, refresh mechanismus
function validateToken(token) {
    // Váš kód zde
}
```

Programátor tak musí sám promyslet bezpečnostní aspekty a implementovat řešení, místo aby pasivně přijal automaticky generovaný kód.

## Aktivace a přizpůsobení

Vzdělávací režim se aktivuje příkazem `/output-style` v Claude Code s následným výběrem preferovaného stylu učení. Nástroj navíc umožňuje vytváření vlastních výukových stylů, které mohou odpovídat specifickým potřebám týmu nebo projektu.

Podle vývojáře Drew Benta z Anthropic, který funkci vyvinul společně s Dicksonem Tsaiem, nový přístup mění programátory z pasivních konzumentů na aktivní účastníky procesu tvorby kódu. Bent uvádí, že používání tohoto režimu mu znovu vrátilo nadšení pro programování a zjednodušilo lidské kontroly kódu generovaného Claude Code.

## Význam pro vzdělávání

Nová funkce představuje pokus o řešení problému, který provází všechny nástroje automatizovaného programování - tendenci uživatelů spoléhat se výhradně na automaticky generovaný kód bez hlubšího porozumění principům. Vzdělávací režim nutí programátory udržet si aktivní přístup k řešení problémů a rozvíjet své dovednosti i při používání pokročilých nástrojů umělé inteligence.

Anthropic tak reaguje na rostoucí obavy z toho, že generativní nástroje mohou vést k degradaci programátorských dovedností. Místo úplné automatizace nabízí hybridní přístup, který kombinuje efektivitu umělé inteligence s lidským učením a kontrolou nad výsledným kódem.