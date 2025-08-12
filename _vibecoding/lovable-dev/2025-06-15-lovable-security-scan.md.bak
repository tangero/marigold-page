---
author: Patrick Zandl
categories:
- AI
- Bezpečnost
- No-code
- Lovable
- Supabase
layout: post
post_excerpt: Platforma Lovable přidala automatické bezpečnostní skenování, AI revizoře a ochranu API klíčů pro bezpečnější vývoj aplikací bez programování.
summary_points:
- Lovable integroval Supabase Security Advisor pro kontrolu databázových politik
- AI-powered Security Reviewer analyzuje celou aplikaci a navrhuje opravy zranitelností
- Automatická ochrana blokuje denně 1200 pokusů o vložení privátních API klíčů do kódu
- Funkce pokrývají SQL injection, XSS útoky a problémy s autentizací
- Bezpečnostní kontroly probíhají před publikováním aplikace
- Všechny API klíče se ukládají jako tajné proměnné v Supabase
date: 2025-06-15
title: Lovable rozšiřuje bezpečnostní funkce pro tvorbu aplikací bez kódování
---

Platforma Lovable pro tvorbu aplikací bez programování přidala tři bezpečnostní funkce k ochraně citlivých dat. Změny zahrnují automatické skenování, AI revizoře kódu a blokování nebezpečného vkládání API klíčů.

## Automatické bezpečnostní skenování

Lovable kontroluje aplikace před zveřejněním pomocí Supabase Security Advisor. Skenování se zaměřuje na Row Level Security (RLS) politiky - SQL pravidla řízení přístupu k databázi. Systém identifikuje chybějící nebo příliš široké politiky, které by umožnily neoprávněný přístup k datům.

## AI revizor zranitelností

Security Reviewer analyzuje celý kód aplikace a hledá širší spektrum bezpečnostních problémů:

- **SQL injection útoky** - nebezpečné vkládání SQL kódu
- **Cross-site scripting (XSS)** - útoky škodlivým JavaScriptem  
- **Problémy s autentizací** - nedostatečné ověřování uživatelů
- **Nechráněné API endpointy** - veřejně přístupné funkce
- **Hardkódované API klíče** - tajné údaje ve zdrojovém kódu

Systém nejen identifikuje problémy, ale navrhuje konkrétní opravy podle architektury aplikace. REviewer se spouští před Publikováním projektu, kdy se nabízí jako speciální tlačítko. SR projde kód i návrh a odhalí spoustu zranitelností. Přes víkend jsem s Lovable hodně dělal a SR fungovalo opravdu skvěle. Odchytalo věci, které jinak samotnému systému přišly v pořádku, jako třeba připojit se na databázi read/write heslem z prohlížeče, navrhlo opravy a samo je opravilo. Opravdu velké zlepšení!

## Automatická ochrana API klíčů

Lovable blokuje vkládání privátních API klíčů do kódu - denně zablokuje 1200 takových pokusů. Všechny klíče se ukládají jako tajné proměnné v Supabase pomocí tlačítka "Add Key" nebo ručně v sekci "Edge Functions".


Další informace jsou v [oficiální dokumentaci Lovable](https://lovable.dev) a [Supabase Security Advisor](https://supabase.com/docs/guides/database/security-advisor).