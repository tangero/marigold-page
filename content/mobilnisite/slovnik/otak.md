---
slug: "otak"
url: "/mobilnisite/slovnik/otak/"
type: "slovnik"
title: "OTAK – Over-The-Air-Key Management (TETRA)"
date: 2026-01-01
abbr: "OTAK"
fullName: "Over-The-Air-Key Management (TETRA)"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/otak/"
summary: "Bezpečnostní mechanismus pro správu kryptografických klíčů přenosem vzduchem v sítích TETRA. Umožňuje bezpečnou distribuci a aktualizaci šifrovacích klíčů do mobilních zařízení, čímž zajišťuje důvěrno"
---

OTAK je bezpečnostní mechanismus TETRA pro správu, distribuci a aktualizaci kryptografických klíčů přenosem vzduchem (over-the-air) za účelem zajištění důvěrnosti a integrity komunikace.

## Popis

Over-The-Air-Key Management (OTAK) je standardizovaný bezpečnostní postup definovaný ve specifikacích 3GPP pro systémy Terrestrial Trunked Radio (TETRA). TETRA je standard digitální mobilní radiokomunikace široce používaný organizacemi veřejné bezpečnosti, dopravními službami a energetickými společnostmi pro klíčovou hlasovou a datovou komunikaci. OTAK funguje v rámci bezpečnostní architektury TETRA a konkrétně řeší správu životního cyklu kryptografických klíčů používaných pro šifrování rozhraní vzduchem (AIE) a šifrování end-to-end ([E2EE](/mobilnisite/slovnik/e2ee/)). Jeho hlavní funkcí je bezpečné doručení nových nebo aktualizovaných šifrovacích klíčů z Key Management Facility (KMF) do mobilních stanic ([MS](/mobilnisite/slovnik/ms/)) nebo terminálů TETRA bez nutnosti fyzického přístupu k zařízení.

Architektura zahrnuje několik klíčových entit: Key Management Facility (KMF), což je důvěryhodná autorita generující a distribuující klíče; infrastrukturu TETRA včetně základnových stanic (TBS) a přepínací a řídicí infrastruktury (SwMI); a mobilní stanici TETRA (MS). KMF využívá existující signalizační kanály TETRA k přenosu zpráv pro správu klíčů. Tyto zprávy jsou samy chráněny pomocí existujících klíčů nebo hierarchie klíčů, čímž je zajištěno bezpečné doručení nového klíčového materiálu. Proces typicky zahrnuje šifrování nového klíče pro šifrování provozu (TEK) nebo skupinového klíče pomocí klíče pro šifrování klíčů ([KEK](/mobilnisite/slovnik/kek/)), který je již bezpečně uložen v mobilní stanici.

Postupy OTAK jsou definovány pro zvládnutí různých scénářů, včetně počátečního zřízení klíčů, periodických aktualizací klíčů pro zvýšení bezpečnosti (rekeying) a nouzového odvolání klíče v případě jeho kompromitace. Protokol zajišťuje, že klíče obdrží pouze autorizovaná zařízení, často s využitím identifikátorů jako je TETRA Subscriber Identity (TSI) a skupinových identifikátorů. Úspěšné doručení a aktivace nového klíče je potvrzeno mobilní stanicí zpět do KMF, což poskytuje jistotu ohledně procesu správy klíčů. Tato možnost přenosu vzduchem je klíčová pro velké flotily zařízení, kde je manuální načítání klíčů nepraktické, a umožňuje škálovatelnou a rychlou správu zabezpečení pro sítě klíčové komunikace.

## K čemu slouží

OTAK byl vytvořen, aby řešil významné provozní a bezpečnostní výzvy manuální správy klíčů ve velkých profesionálních mobilních radiových systémech, jako je TETRA. Před zavedením OTAK byly kryptografické klíče často do radiostanic nahrávány pomocí fyzických připojení (např. zařízení pro naplnění klíčů nebo kabelů), což je proces časově náročný, logisticky obtížný a náchylný k chybám u organizací se stovkami či tisíci nasazených zařízení. Pro operátory veřejné bezpečnosti a kritické infrastruktury představovala nemožnost rychlé změny šifrovacích klíčů v celé flotile závažnou bezpečnostní slabinu, zejména pokud bylo zařízení ztraceno, ukradeno nebo existovalo podezření na kompromitaci klíče.

Motivace pro OTAK vychází z potřeby dynamické, vzdálené správy zabezpečení, která odpovídá provoznímu tempu moderní klíčové komunikace. Řeší problém udržení kryptografické agilnosti – schopnosti rychle měnit šifrovací algoritmy nebo klíče v reakci na vyvíjející se hrozby. Díky možnosti aktualizací přenosem vzduchem umožňuje OTAK správcům sítě vynucovat bezpečnostní politiky, provádět pravidelné rotace klíčů za účelem omezení dopadu potenciální kryptoanalýzy a okamžitě zneplatnit klíče v celé síti během bezpečnostních incidentů. Tato schopnost je zásadní pro udržení dlouhodobé důvěrnosti citlivé komunikace ve vládních, záchranných a průmyslových aplikacích spoléhajících na technologii TETRA.

## Klíčové vlastnosti

- Bezpečná vzdálená distribuce klíčů pro šifrování provozu (TEKs) a skupinových klíčů
- Využívá hierarchii klíčů (např. KEKs) k ochraně procesu doručení klíče
- Podporuje postupy pro počáteční zřízení klíčů, periodické obnovování klíčů (rekeying) a nouzové odvolání klíčů
- Funguje přes standardní signalizační kanály TETRA bez nutnosti vyhrazených datových relací
- Zahrnuje potvrzovací mechanismy z mobilní stanice pro potvrzení přijetí a aktivace klíče
- Integruje se s autentizačními a infrastrukturními bezpečnostními mechanismy TETRA

## Definující specifikace

- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TR 23.783** (Rel-18) — Technical Report on Mission Critical Services over 5GS
- **TS 24.883** (Rel-16) — MCPTT Interworking with LMR Systems

---

📖 **Anglický originál a plná specifikace:** [OTAK na 3GPP Explorer](https://3gpp-explorer.com/glossary/otak/)
