---
author: Patrick Zandl
categories:
- AI
- Google
- platby
- agenti
- kryptoměny
- stablecoiny
layout: post
post_excerpt: Google  představil Agent Payments Protocol (AP2) s rozšířením x402, které umožňuje AI agentům provádět platby pomocí stablecoinů. Podporu poskytuje 60+ partnerů včetně Coinbase a PayPal. O co jde? 
summary_points:
- Google představil 16. září 2025 Agent Payments Protocol (AP2) pro platby iniciované AI agenty
- Rozšíření x402 od Coinbase umožňuje agentům platit pomocí stablecoinů jako USDC
- Podporu poskytuje více než 60 organizací včetně Mastercard, PayPal, American Express
- AP2 využívá kryptograficky podepsané "mandáty" pro autorizaci transakcí
- Protokol podporuje jak tradiční platební metody, tak kryptoměny
- Ethereum Foundation spolupracuje na standardu ERC-8004 pro blockchain transakce agentů
title: Google představil platební protokol AP2 s podporou stablecoinů pro AI agenty
---

Google představil Agent Payments Protocol (AP2), otevřený protokol umožňující AI agentům provádět bezpečné platby jménem uživatelů. Novinka rozšiřuje již existující Agent2Agent (A2A) protokol o klíčovou platební funkcionalitu a získala podporu více než 60 technologických a finančních společností včetně Mastercard, PayPal, American Express, Coinbase a Ethereum Foundation. Protokol je také zajímavým koketováním Google s kryptoměnovou scénou, navíc velmi dobře pochopitelným. 

AP2 řeší základní problém současných AI agentů, kteří dokážou najít produkty, porovnat ceny nebo připravit nákupní košík, ale nemohou dokončit transakci. Nový protokol vytváří standardizovaný rámec pro bezpečné provedení platby přímo agentem bez nutnosti lidského zásahu při každé transakci.

## Bezpečnostní mechanismus mandátů

Klíčovým prvkem protokolu AP2 jsou "mandáty" - kryptograficky podepsané digitální smlouvy, které slouží jako ověřitelný důkaz uživatelových instrukcí. Systém rozlišuje dva typy mandátů podle způsobu nakupování:

**Nákupy v reálném čase** vyžadují dvojí schválení. Nejprve uživatel poskytne "záměrný mandát" (Intent Mandate), například "najdi mi nové bílé běžecké boty", který agentovi umožní vyhledávat a vyjednávat. Po prezentaci vhodných možností uživatel udělí "košíkový mandát" (Cart Mandate) jako finální souhlas s konkrétní koupí.

**Delegované úkoly** fungují s detailním záměrným mandátem předem. Uživatel může zadat pokyn typu "kup vstupenky na koncert ve chvíli, kdy půjdou do prodeje" s přesnými cenami, časováním a dalšími pravidly. Agent pak může provést nákup autonomně bez dalšího schvalování.

## Rozšíření x402 pro kryptoplaty

Společnost Coinbase vytvořila rozšíření x402, které do protokolu AP2 integruje podporu pro stablecoiny. Toto rozšíření umožňuje agentům provádět platby pomocí kryptoměn jako USDC s okamžitým vypořádáním a nižším rizikem podvodů.

> **Stablecoiny** jsou kryptoměny navázané na stabilní hodnotu (typicky 1:1 k americkému dolaru), které kombinují rychlost a transparentnost blockchainových transakcí s cenovou stabilitou tradičních měn - na rozdíl od volatilních kryptoměn jako Bitcoin zachovávají konstantní hodnotu, což je činí vhodnými pro běžné platby.

Výhody stablecoinových plateb zahrnují:
- Okamžité vypořádání transakcí bez čekání na bankovní převody
- Nižší poplatky než tradiční mezinárodní platby
- Transparentní blockchain záznam jako doklad o nákupu
- Možnost platby jedním dotykem bez zadávání čísla karty

Brian Armstrong, generální ředitel Coinbase, k novince uvedl: "x402 + Google právě odemkly novou úroveň pro AI agenty. Agenti si nyní mohou skutečně vzájemně platit pomocí x402, které pohání stablecoinovou infrastrukturu uvnitř Google's nového Agentic Payments Protocol (AP2)."

## Podporovaní partneři a ekosystém

AP2 získal podporu širokého spektra finančních a technologických společností:

**Platební společnosti**: Mastercard, American Express, PayPal, Revolut, JCB, UnionPay International, Worldpay
**Krypto firmy**: Coinbase, Ethereum Foundation, MetaMask, Mysten Labs, Ant International
**Obchodní platformy**: Etsy, Salesforce, ServiceNow, Intuit
**Bezpečnostní firmy**: Adyen, Forter

Pablo Fourez z Mastercard projekt komentoval: "AP2 formuje budoucnost agentní obchodní činnosti a zdůrazňuje, že budování standardů a důvěry bude vyžadovat čas a spolupráci."

## Praktická demonstrace

Google a Coinbase vytvořili demonstraci nákupu ledničky prostřednictvím AI agenta. Proces zahrnuje:
1. Uživatel zadá požadavek na nákup spotřebiče
2. Agent vyhledá dostupné možnosti a porovná ceny
3. Prezentuje doporučení s cenami a specifikacemi
4. Po schválení provede platbu pomocí x402 a stablecoinů
5. Zajistí doručení a poskytne blockchain účtenku

Demonstrace ukazuje, jak AI agent zvládne kompletní nákupní proces od vyhledávání až po finální transakci během jedné konverzace.

## Součinnost s Ethereum ekosystémem

Ethereum Foundation aktivně spolupracuje na standardu ERC-8004, který definuje způsob, jak si agenti na Ethereum síti navzájem objevují, ověřují identity a provádějí transakce. Davide Crapis, vedoucí AI týmu Ethereum Foundation, vysvětlil: "ERC-8004 bude podporovat mnoho forem plateb, ale rozšíření x402 pomáhá zlepšit vývojářskou zkušenost."

Standard ERC-8004 doplňuje rozšíření x402 tím, že poskytuje blockchain infrastrukturu pro objevování a ověřování agentů, zatímco x402 zjednodušuje vývojářskou implementaci platebních funkcí.

## Technické požadavky implementace

Protokol AP2 vyžaduje:
- HTTPS připojení s moderním TLS
- Podporu pro JSON-RPC 2.0 komunikaci
- Implementaci kryptografického podpisování mandátů
- Kompatibilitu s existujícími platebními bránami

Google zveřejnil úplnou technickou specifikaci na [GitHub repositáři](https://github.com/google/agent-payments-protocol) spolu s referenčními implementacemi pro různé programovací jazyky.

## Srovnání s konkurencí

Zatímco společnosti jako Perplexity nabízejí službu "Buy With Pro" ve svém agentním prohlížeči a Stripe poskytuje nástroje pro agentní nákupy, AP2 představuje komplexnější řešení s širší podporou platebních metod a partnerů.

Klíčovým rozdílem je AP2 fokus na otevřenost a interoperabilitu - protokol není vázán na konkrétní platformu nebo platební systém, což umožňuje jeho adopci napříč různými AI frameworky a obchodními systémy.

## Regulační aspekty a bezpečnost

AP2 se zavazuje k dodržování průmyslových pravidel a standardů. Protokol adresuje tři klíčové bezpečnostní otázky:

**Autorizace**: Ověření, že uživatel skutečně agentovi udělil oprávnění k provedení konkrétního nákupu prostřednictvím kryptografických mandátů.

**Autenticita**: Zajištění, že požadavek agenta přesně odráží skutečný záměr uživatele prostřednictvím strukturovaných mandátů s jasnými parametry.

**Odpovědnost**: Vytvoření auditovatelné stopy pro případ podvodných nebo nesprávných transakcí s možností zpětného dohledání všech kroků.

## Budoucí vývoj a dostupnost

Google plánuje postupné rozšiřování AP2 protokolu s podporou dalších platebních metod a regionálních standardů. Společnost zdůraznila otevřený a kolaborativní přístup k vývoju s možností zapojení celé platební a technologické komunity.

Agenti s podporou AP2 budou dostupní v Google AI Agent Marketplace, což vytvoří centrální místo pro objevování a používání platebních agentů. Podnikové aplikace mohou využít AP2 například pro autonomní nákup partnerských řešení přes Google Cloud Marketplace nebo automatické škálování softwarových licencí podle aktuálních potřeb. Je tedy zřejmé, proč Google s takovým řešením přišel - blíže se přisaje k platebním mechanismům, což je část internetu, kterou doposud neměl moc podchycenou. Agentní platby mu to umožní změnit. 

Protokol AP2 s rozšířením x402 představuje významný krok směrem k autonomní digitální ekonomice, kde AI agenti mohou nejen komunikovat a spolupracovat, ale také samostatně provádět ekonomické transakce. Široká podpora ze strany finančních i technologických gigantů naznačuje potenciál pro rychlou adopci a standardizaci agentních plateb v nadcházejících letech. Až si příště [budu kupovat lístky do divadla pomocí AI agenta](https://www.marigold.cz/item/nehoda-ai-agenta/), už to dopadne...uplně stejně, co myslíte 😎