---
slug: "sha-3"
url: "/mobilnisite/slovnik/sha-3/"
type: "slovnik"
title: "SHA-3 – Secure Hash Algorithm 3"
date: 2025-01-01
abbr: "SHA-3"
fullName: "Secure Hash Algorithm 3"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/sha-3/"
summary: "SHA-3 je standard kryptografické hashovací funkce (Keccak) vyvinutý NIST jako budoucně odolný nástupce SHA-2. V 3GPP je specifikován jako volitelný algoritmus pro zvýšenou odolnost zabezpečení, nabíze"
---

SHA-3 je standard kryptografické hashovací funkce specifikovaný 3GPP jako volitelný, strukturně odlišný algoritmus založený na houbové konstrukci (sponge construction) pro zajištění zvýšené odolnosti zabezpečení pro integritu a autentizaci.

## Popis

SHA-3, standardizovaný [NIST](/mobilnisite/slovnik/nist/) jako [FIPS](/mobilnisite/slovnik/fips/) PUB 202, je rodina kryptografických hashovacích funkcí odvozená z algoritmu Keccak, který vyhrál soutěž NIST na hashovací funkci. Na rozdíl od Merkle-Damgårdovy struktury [SHA-2](/mobilnisite/slovnik/sha-2/) je SHA-3 postaven na houbové konstrukci (sponge construction), která nabízí přirozenou odolnost proti útokům prodlužování zpráv (length-extension attacks) a poskytuje flexibilní rámec pro hashování, autentizované šifrování a generování pseudonáhodných čísel. Jádrem SHA-3 je permutační funkce pracující na stavovém poli bitů, kde kapacita (capacity) a rychlost (rate) určují zabezpečení a výkon. Varianty zahrnují SHA3-224, SHA3-256, SHA3-384, SHA3-512 a funkce s rozšiřitelným výstupem (SHAKE128, SHAKE256).

V systémech 3GPP, jak je specifikováno v TS 35.934, je SHA-3 zahrnuto jako součást portfolia kryptografických algoritmů pro budoucí odolnost zabezpečení sítě. Jeho činnost zahrnuje absorbování vstupních dat do houbového stavu pomocí operací XOR, iterativní aplikaci Keccak-f permutace a následné vytlačení požadované délky hashe. Tento proces poskytuje robustní bezpečnostní rezervu díky velkému vnitřnímu stavu a absenci známých strukturních slabin podobných těm u starších hashovacích funkcí. Pro mobilní sítě by mohl být SHA-3 integrován do algoritmů ochrany integrity pro vrstvu [PDCP](/mobilnisite/slovnik/pdcp/), do funkcí odvozování klíčů v rámci autentizačních protokolů a do mechanismů ověřování certifikátů, ačkoli jeho adopce v nasazených systémech je ve srovnání se SHA-256 pomalejší.

Specifikace podrobně popisuje parametry algoritmu a jeho potenciální aplikaci v kontextech zabezpečení Universal Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)) a Evolved UTRAN ([E-UTRAN](/mobilnisite/slovnik/e-utran/)). Návrh SHA-3 umožňuje paralelizaci a efektivní hardwarovou implementaci, což je výhodné pro vysokokapacitní 5G core sítě a zařízení IoT s omezenými prostředky. Ačkoli ještě není povinný v hlavních bezpečnostních profilech 3GPP, jeho zařazení zajišťuje, aby operátoři měli ověřenou alternativu, pokud by budoucí kryptoanalýza ohrozila SHA-2, což je v souladu s principem kryptografické flexibility nezbytným pro dlouhodobý vývoj sítě.

## K čemu slouží

SHA-3 byl vyvinut [NIST](/mobilnisite/slovnik/nist/) za účelem poskytnutí různorodého standardu kryptografické hashovací funkce, což zajišťuje záložní možnost, pokud by se [SHA-2](/mobilnisite/slovnik/sha-2/) stalo ohroženým v důsledku pokroků v kryptoanalýze. Motivací pro jeho zařazení do 3GPP, počínaje Release 12, bylo zajistit budoucí odolnost zabezpečení mobilních sítí začleněním algoritmu s naprosto odlišným matematickým základem než SHA-2. Tím se řeší riziko, že jediná strukturní zranitelnost by mohla ovlivnit všechny široce nasazené hashovací funkce.

Houbová konstrukce SHA-3 nabízí teoretické výhody, jako je imunita vůči útokům prodlužování zpráv a přímočařejší bezpečnostní důkaz, což byly limity v Merkle-Damgårdově návrhu SHA-2. Pro 3GPP to poskytuje volitelný, robustní primitiv pro požadavky zabezpečení příští generace, zejména pro 5G a další, kde jsou zvažovány hrozby kvantových počítačů a pokročilé modely útoků. Flexibilita SHA-3 podporuje nejen hashování, ale také režimy autentizovaného šifrování, což by mohlo zjednodušit návrh bezpečnostních protokolů. Jeho adopce odráží proaktivní přístup 3GPP ke kryptografické odolnosti, zajišťující, že mobilní sítě mohou udržet záruky integrity a autentizace i tváří v tvář vyvíjejícím se kryptografickým hrozbám.

## Klíčové vlastnosti

- Založeno na houbové konstrukci Keccak, nikoli na Merkle-Damgård
- Poskytuje varianty SHA3-224, SHA3-256, SHA3-384, SHA3-512
- Zahrnuje funkce s rozšiřitelným výstupem (SHAKE128, SHAKE256)
- Přirozená odolnost proti útokům prodlužování zpráv (length-extension attacks)
- Vhodné pro hardwarovou implementaci a paralelní zpracování
- Standardizováno NIST ve FIPS 202 a referencováno v 3GPP TS 35.934

## Definující specifikace

- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [SHA-3 na 3GPP Explorer](https://3gpp-explorer.com/glossary/sha-3/)
