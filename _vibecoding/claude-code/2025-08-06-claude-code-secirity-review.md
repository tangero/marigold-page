---
author: Patrick Zandl
categories:
- AI
- Anthropic
- Claude Code
- bezpečnost
- GitHub
layout: vibecoding-default
post_excerpt: Anthropic přidal do Claude Code automatické bezpečnostní kontroly kódu přímo v terminálu a integraci s GitHub Actions pro kontrolu každého PR.
summary_points:
- Claude Code získal nový příkaz /security-review pro okamžité bezpečnostní kontroly
- GitHub Actions integrace automaticky kontroluje každý PR na zranitelnosti
- Systém detekuje SQL injection, XSS útoky a nebezpečné zacházení s daty
- Anthropic používá nástroj interně a zachytil skutečné bezpečnostní hrozby
- Claude dokáže nalezené zranitelnosti rovnou opravit
- Integrace přidává komentáře přímo do kódu s vysvětlením a návrhy oprav
title: Claude Code přidává automatické bezpečnostní kontroly kódu
---

Společnost Anthropic rozšířila svůj nástroj Claude Code o automatické bezpečnostní kontroly kódu. Nová funkcionalita umožňuje vývojářům odhalit zranitelnosti ještě před nasazením do produkce prostřednictvím dvou hlavních komponent: příkazu pro okamžité kontroly přímo z terminálu a integrace s platformou GitHub Actions pro automatickou analýzu každého požadavku na sloučení kódu.

## Příkaz /security-review pro okamžitou analýzu

Nový příkaz `/security-review` provádí bezpečnostní analýzu přímo z vývojářského terminálu. Po spuštění příkazu Claude analyzuje kód a hledá běžné bezpečnostní zranitelnosti. Systém se zaměřuje na detekci rizik SQL injection, což jsou útoky umožňující neoprávněnou manipulaci s databází prostřednictvím škodlivého SQL kódu vloženého do vstupních polí aplikace. Dále kontroluje zranitelnosti typu XSS (Cross-Site Scripting), kdy útočník může vložit škodlivý skript do webové stránky zobrazované ostatním uživatelům. Claude také identifikuje případy nebezpečného zacházení s daty, jako je ukládání hesel v nešifrované podobě nebo nedostatečná validace uživatelských vstupů.

Pokud Claude objeví zranitelnost, může ji na požádání vývojáře rovnou opravit. Tato schopnost výrazně zrychluje proces zabezpečení kódu, protože vývojář nemusí zranitelnost opravovat ručně, ale může využít návrh opravy generovaný umělou inteligencí. Pro použití této funkce stačí aktualizovat Claude Code na nejnovější verzi a spustit příkaz přímo v terminálu.

## Integrace s GitHub Actions

Druhá komponenta představuje integraci s platformou GitHub Actions, která automatizuje bezpečnostní kontroly při práci s verzovacím systémem Git. GitHub Actions je služba pro automatizaci vývojových procesů, která umožňuje spouštět různé úlohy při specifických událostech v repozitáři, například při vytvoření nového požadavku na sloučení kódu (pull request).

Po konfiguraci integrace systém automaticky kontroluje každý nový požadavek na sloučení a hledá potenciální bezpečnostní problémy. Výsledky analýzy se zobrazují přímo v rozhraní GitHubu formou komentářů u konkrétních řádků kódu, kde byla zranitelnost detekována. Každý komentář obsahuje vysvětlení problému a doporučené řešení, což usnadňuje vývojářům pochopení a opravu nalezených problémů.

Integrace funguje jako automatický bezpečnostní recenzent, který kontroluje každou změnu kódu ještě před jejím začleněním do hlavní větve projektu. Tím se výrazně snižuje riziko, že se do produkční verze aplikace dostane kód obsahující bezpečnostní zranitelnosti.

## Praktické nasazení a výsledky

Anthropic využívá tuto technologii interně pro vlastní projekty. Podle oznámení společnosti systém již zachytil skutečné bezpečnostní hrozby, včetně potenciální zranitelnosti umožňující vzdálené spuštění kódu (Remote Code Execution - RCE) v interním nástroji. Zranitelnost RCE patří mezi nejzávažnější bezpečnostní problémy, protože umožňuje útočníkovi spustit libovolný kód na cílovém systému, což může vést k úplnému převzetí kontroly nad serverem nebo aplikací.

Díky automatické kontrole prostřednictvím GitHub Actions byla tato zranitelnost odhalena a opravena ještě před nasazením do produkčního prostředí. Tento příklad demonstruje praktickou hodnotu nástroje v reálném vývojovém procesu, kde dokáže zachytit i závažné bezpečnostní problémy, které by mohly mít vážné důsledky.

## Technická implementace a dostupnost

Pro začátek práce s příkazem `/security-review` je potřeba pouze aktualizovat Claude Code na nejnovější verzi. Příkaz je poté dostupný přímo v terminálu a může být spuštěn kdykoliv během vývoje pro okamžitou kontrolu aktuálního kódu.

Implementace GitHub Actions vyžaduje přidání konfiguračního souboru do repozitáře projektu. Anthropic poskytuje dokumentaci a ukázkovou konfiguraci na [GitHub repozitáři claude-code-security-review](https://github.com/anthropics/claude-code-security-review), který obsahuje podrobné instrukce pro nastavení automatických kontrol. Konfigurace definuje, kdy se má kontrola spustit (typicky při vytvoření nebo aktualizaci požadavku na sloučení) a jaké části kódu mají být analyzovány.

Nástroj představuje praktické využití umělé inteligence v oblasti kybernetické bezpečnosti, kde může výrazně zvýšit kvalitu kódu tím, že automaticky identifikuje potenciální bezpečnostní problémy dříve, než se dostanou do produkce. Kombinace okamžitých kontrol během vývoje a automatických kontrol při revizi kódu vytváří vícevrstvý bezpečnostní systém, který pomáhá udržovat vysokou úroveň zabezpečení aplikací.