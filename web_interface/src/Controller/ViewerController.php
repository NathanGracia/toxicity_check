<?php

namespace App\Controller;

use App\Entity\Viewer;
use App\Form\ViewerType;
use App\Repository\ViewerRepository;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

#[Route('/viewer')]
class ViewerController extends AbstractController
{
    #[Route('/', name: 'app_viewer_index', methods: ['GET'])]
    public function index(ViewerRepository $viewerRepository): Response
    {
        return $this->render('viewer/index.html.twig', [
            'viewers' => $viewerRepository->findAll(),
        ]);
    }

    #[Route('/new', name: 'app_viewer_new', methods: ['GET', 'POST'])]
    public function new(Request $request, ViewerRepository $viewerRepository): Response
    {
        $viewer = new Viewer();
        $form = $this->createForm(ViewerType::class, $viewer);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $viewerRepository->save($viewer, true);

            return $this->redirectToRoute('app_viewer_index', [], Response::HTTP_SEE_OTHER);
        }

        return $this->renderForm('viewer/new.html.twig', [
            'viewer' => $viewer,
            'form' => $form,
        ]);
    }

    #[Route('/{id}', name: 'app_viewer_show', methods: ['GET'])]
    public function show(Viewer $viewer): Response
    {
        return $this->render('viewer/show.html.twig', [
            'viewer' => $viewer,
        ]);
    }

    #[Route('/{id}/edit', name: 'app_viewer_edit', methods: ['GET', 'POST'])]
    public function edit(Request $request, Viewer $viewer, ViewerRepository $viewerRepository): Response
    {
        $form = $this->createForm(ViewerType::class, $viewer);
        $form->handleRequest($request);

        if ($form->isSubmitted() && $form->isValid()) {
            $viewerRepository->save($viewer, true);

            return $this->redirectToRoute('app_viewer_index', [], Response::HTTP_SEE_OTHER);
        }

        return $this->renderForm('viewer/edit.html.twig', [
            'viewer' => $viewer,
            'form' => $form,
        ]);
    }

    #[Route('/{id}', name: 'app_viewer_delete', methods: ['POST'])]
    public function delete(Request $request, Viewer $viewer, ViewerRepository $viewerRepository): Response
    {
        if ($this->isCsrfTokenValid('delete'.$viewer->getId(), $request->request->get('_token'))) {
            $viewerRepository->remove($viewer, true);
        }

        return $this->redirectToRoute('app_viewer_index', [], Response::HTTP_SEE_OTHER);
    }
}
